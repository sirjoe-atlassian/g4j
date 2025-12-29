#!/usr/bin/env python3
"""
Test Automation Code Generator

This module provides utilities to automatically generate test cases
from templates and specifications.
"""

import os
import json
from typing import Dict, List, Optional
from datetime import datetime


class TestGenerator:
    """Generates test code from templates and specifications."""
    
    def __init__(self, output_dir: str = "generated_tests"):
        """
        Initialize the test generator.
        
        Args:
            output_dir: Directory where generated tests will be saved
        """
        self.output_dir = output_dir
        self.templates = {}
        
    def register_template(self, name: str, template: str):
        """
        Register a test template.
        
        Args:
            name: Name of the template
            template: Template string with placeholders
        """
        self.templates[name] = template
    
    def generate_test(self, template_name: str, test_spec: Dict) -> str:
        """
        Generate test code from a template and specification.
        
        Args:
            template_name: Name of the registered template to use
            test_spec: Dictionary containing test parameters
            
        Returns:
            Generated test code as a string
        """
        if template_name not in self.templates:
            raise ValueError(f"Template '{template_name}' not found")
        
        template = self.templates[template_name]
        
        # Replace placeholders with values from test_spec
        generated_code = template
        for key, value in test_spec.items():
            placeholder = "{" + key + "}"
            generated_code = generated_code.replace(placeholder, str(value))
        
        return generated_code
    
    def generate_test_suite(self, template_name: str, test_specs: List[Dict], 
                           suite_name: str) -> str:
        """
        Generate a complete test suite from multiple test specifications.
        
        Args:
            template_name: Name of the template to use
            test_specs: List of test specifications
            suite_name: Name of the test suite
            
        Returns:
            Generated test suite code
        """
        generated_tests = []
        
        for spec in test_specs:
            test_code = self.generate_test(template_name, spec)
            generated_tests.append(test_code)
        
        suite_header = f'''"""
{suite_name}
Auto-generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""

import unittest

'''
        
        suite_body = "\n\n".join(generated_tests)
        
        suite_footer = '''

if __name__ == '__main__':
    unittest.main()
'''
        
        return suite_header + suite_body + suite_footer
    
    def save_test_suite(self, code: str, filename: str):
        """
        Save generated test suite to a file.
        
        Args:
            code: Generated test code
            filename: Name of the file to save to
        """
        os.makedirs(self.output_dir, exist_ok=True)
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w') as f:
            f.write(code)
        
        print(f"Test suite saved to: {filepath}")
        return filepath


# Predefined templates
UNIT_TEST_TEMPLATE = '''class Test{class_name}(unittest.TestCase):
    """Test cases for {class_name}"""
    
    def test_{test_name}(self):
        """Test {test_description}"""
        # Arrange
        {setup_code}
        
        # Act
        {action_code}
        
        # Assert
        {assertion_code}'''


API_TEST_TEMPLATE = '''class Test{api_name}API(unittest.TestCase):
    """API test cases for {api_name}"""
    
    def test_{test_name}(self):
        """Test {test_description}"""
        # Setup
        url = "{endpoint}"
        payload = {payload}
        
        # Execute request
        response = requests.{method}(url, json=payload)
        
        # Verify
        self.assertEqual(response.status_code, {expected_status})
        {additional_assertions}'''


def load_test_specs_from_json(filepath: str) -> List[Dict]:
    """
    Load test specifications from a JSON file.
    
    Args:
        filepath: Path to JSON file containing test specs
        
    Returns:
        List of test specification dictionaries
    """
    with open(filepath, 'r') as f:
        return json.load(f)


def main():
    """Example usage of the test generator."""
    generator = TestGenerator()
    
    # Register templates
    generator.register_template("unit_test", UNIT_TEST_TEMPLATE)
    generator.register_template("api_test", API_TEST_TEMPLATE)
    
    # Example test specifications
    test_specs = [
        {
            "class_name": "Calculator",
            "test_name": "addition",
            "test_description": "addition of two numbers",
            "setup_code": "calc = Calculator()",
            "action_code": "result = calc.add(2, 3)",
            "assertion_code": "self.assertEqual(result, 5)"
        },
        {
            "class_name": "Calculator",
            "test_name": "subtraction",
            "test_description": "subtraction of two numbers",
            "setup_code": "calc = Calculator()",
            "action_code": "result = calc.subtract(5, 3)",
            "assertion_code": "self.assertEqual(result, 2)"
        }
    ]
    
    # Generate test suite
    suite_code = generator.generate_test_suite(
        "unit_test", 
        test_specs, 
        "Calculator Test Suite"
    )
    
    # Save to file
    generator.save_test_suite(suite_code, "test_calculator.py")
    print("\nGenerated test suite successfully!")


if __name__ == "__main__":
    main()

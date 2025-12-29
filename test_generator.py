"""
Test Automation Code Generator

This module provides functionality to automatically generate test cases
based on various input formats and requirements.
"""

import os
import json
from typing import List, Dict, Any, Optional
from datetime import datetime


class TestGenerator:
    """
    A class to generate automated test code from specifications.
    """
    
    def __init__(self, framework: str = "pytest"):
        """
        Initialize the test generator.
        
        Args:
            framework: The testing framework to use (pytest, unittest, etc.)
        """
        self.framework = framework
        self.tests = []
        
    def generate_test_class(self, class_name: str, test_cases: List[Dict[str, Any]]) -> str:
        """
        Generate a test class with multiple test cases.
        
        Args:
            class_name: Name of the test class
            test_cases: List of test case specifications
            
        Returns:
            Generated test code as a string
        """
        if self.framework == "pytest":
            return self._generate_pytest_class(class_name, test_cases)
        elif self.framework == "unittest":
            return self._generate_unittest_class(class_name, test_cases)
        else:
            raise ValueError(f"Unsupported framework: {self.framework}")
    
    def _generate_pytest_class(self, class_name: str, test_cases: List[Dict[str, Any]]) -> str:
        """Generate pytest-style test class."""
        code = f"""import pytest\n\n\nclass {class_name}:\n"""
        code += f'    """Generated test class for {class_name}"""\n\n'
        
        for i, test_case in enumerate(test_cases):
            test_name = test_case.get('name', f'test_case_{i+1}')
            description = test_case.get('description', '')
            inputs = test_case.get('inputs', {})
            expected = test_case.get('expected', None)
            
            code += f"    def test_{test_name}(self):\n"
            if description:
                code += f'        """{description}"""\n'
            
            # Generate test body
            code += f"        # Arrange\n"
            for key, value in inputs.items():
                code += f"        {key} = {repr(value)}\n"
            
            code += f"\n        # Act\n"
            code += f"        # TODO: Add your test logic here\n"
            code += f"        result = None  # Replace with actual function call\n"
            
            code += f"\n        # Assert\n"
            if expected is not None:
                code += f"        assert result == {repr(expected)}\n"
            else:
                code += f"        assert result is not None\n"
            
            code += "\n"
        
        return code
    
    def _generate_unittest_class(self, class_name: str, test_cases: List[Dict[str, Any]]) -> str:
        """Generate unittest-style test class."""
        code = f"""import unittest\n\n\nclass {class_name}(unittest.TestCase):\n"""
        code += f'    """Generated test class for {class_name}"""\n\n'
        
        for i, test_case in enumerate(test_cases):
            test_name = test_case.get('name', f'case_{i+1}')
            description = test_case.get('description', '')
            inputs = test_case.get('inputs', {})
            expected = test_case.get('expected', None)
            
            code += f"    def test_{test_name}(self):\n"
            if description:
                code += f'        """{description}"""\n'
            
            # Generate test body
            code += f"        # Arrange\n"
            for key, value in inputs.items():
                code += f"        {key} = {repr(value)}\n"
            
            code += f"\n        # Act\n"
            code += f"        # TODO: Add your test logic here\n"
            code += f"        result = None  # Replace with actual function call\n"
            
            code += f"\n        # Assert\n"
            if expected is not None:
                code += f"        self.assertEqual(result, {repr(expected)})\n"
            else:
                code += f"        self.assertIsNotNone(result)\n"
            
            code += "\n"
        
        code += '\n\nif __name__ == "__main__":\n'
        code += '    unittest.main()\n'
        
        return code
    
    def generate_from_json(self, json_spec: str) -> str:
        """
        Generate test code from JSON specification.
        
        Args:
            json_spec: JSON string containing test specifications
            
        Returns:
            Generated test code
        """
        spec = json.loads(json_spec)
        class_name = spec.get('class_name', 'GeneratedTest')
        test_cases = spec.get('test_cases', [])
        
        return self.generate_test_class(class_name, test_cases)
    
    def save_test_file(self, code: str, filename: str, output_dir: str = "tests") -> str:
        """
        Save generated test code to a file.
        
        Args:
            code: Generated test code
            filename: Name of the output file
            output_dir: Directory to save the file
            
        Returns:
            Path to the saved file
        """
        os.makedirs(output_dir, exist_ok=True)
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w') as f:
            f.write(code)
        
        return filepath


def main():
    """Example usage of the test generator."""
    # Example test specification
    test_spec = {
        "class_name": "TestMathOperations",
        "test_cases": [
            {
                "name": "addition",
                "description": "Test basic addition operation",
                "inputs": {"a": 2, "b": 3},
                "expected": 5
            },
            {
                "name": "subtraction",
                "description": "Test basic subtraction operation",
                "inputs": {"a": 5, "b": 3},
                "expected": 2
            }
        ]
    }
    
    # Generate pytest tests
    generator = TestGenerator(framework="pytest")
    test_code = generator.generate_test_class(
        test_spec['class_name'],
        test_spec['test_cases']
    )
    
    print("Generated Test Code:")
    print("=" * 60)
    print(test_code)
    
    # Save to file
    output_file = generator.save_test_file(test_code, "test_math_operations.py")
    print(f"\nTest file saved to: {output_file}")


if __name__ == "__main__":
    main()

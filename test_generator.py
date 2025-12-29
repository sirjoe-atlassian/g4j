#!/usr/bin/env python3
"""
Test Automation Code Generator
Generates test templates for various testing frameworks
"""

import argparse
import os
from typing import Dict, List


class TestGenerator:
    """Generates test code templates for different testing frameworks."""
    
    def __init__(self):
        self.templates = {
            'pytest': self._generate_pytest_template,
            'unittest': self._generate_unittest_template,
            'jest': self._generate_jest_template,
            'junit': self._generate_junit_template,
        }
    
    def generate(self, framework: str, test_name: str, class_name: str = None, methods: List[str] = None) -> str:
        """
        Generate test code for specified framework.
        
        Args:
            framework: Testing framework (pytest, unittest, jest, junit)
            test_name: Name of the test file/class
            class_name: Name of the class being tested (optional)
            methods: List of methods to generate tests for (optional)
            
        Returns:
            Generated test code as string
        """
        if framework not in self.templates:
            raise ValueError(f"Unsupported framework: {framework}. Supported: {list(self.templates.keys())}")
        
        return self.templates[framework](test_name, class_name, methods or [])
    
    def _generate_pytest_template(self, test_name: str, class_name: str, methods: List[str]) -> str:
        """Generate pytest template."""
        code = f'''"""
Test module for {class_name or test_name}
"""

import pytest


class Test{class_name or test_name.replace('_', '').title()}:
    """Test class for {class_name or test_name}."""
    
    @pytest.fixture
    def setup(self):
        """Set up test fixtures."""
        # Setup code here
        yield
        # Teardown code here
    
'''
        
        if methods:
            for method in methods:
                code += f'''    def test_{method}(self, setup):
        """Test {method} method."""
        # Arrange
        
        # Act
        
        # Assert
        assert True, "Test not implemented"
    
'''
        else:
            code += f'''    def test_example(self, setup):
        """Example test case."""
        # Arrange
        
        # Act
        
        # Assert
        assert True, "Test not implemented"
'''
        
        return code
    
    def _generate_unittest_template(self, test_name: str, class_name: str, methods: List[str]) -> str:
        """Generate unittest template."""
        code = f'''"""
Test module for {class_name or test_name}
"""

import unittest


class Test{class_name or test_name.replace('_', '').title()}(unittest.TestCase):
    """Test class for {class_name or test_name}."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Setup code here
        pass
    
    def tearDown(self):
        """Clean up after tests."""
        # Teardown code here
        pass
    
'''
        
        if methods:
            for method in methods:
                code += f'''    def test_{method}(self):
        """Test {method} method."""
        # Arrange
        
        # Act
        
        # Assert
        self.fail("Test not implemented")
    
'''
        else:
            code += f'''    def test_example(self):
        """Example test case."""
        # Arrange
        
        # Act
        
        # Assert
        self.fail("Test not implemented")


if __name__ == '__main__':
    unittest.main()
'''
        
        return code
    
    def _generate_jest_template(self, test_name: str, class_name: str, methods: List[str]) -> str:
        """Generate Jest (JavaScript) template."""
        code = f'''/**
 * Test suite for {class_name or test_name}
 */

describe('{class_name or test_name}', () => {{
    beforeEach(() => {{
        // Setup code here
    }});
    
    afterEach(() => {{
        // Teardown code here
    }});
    
'''
        
        if methods:
            for method in methods:
                code += f'''    test('{method} should work correctly', () => {{
        // Arrange
        
        // Act
        
        // Assert
        expect(true).toBe(true); // Test not implemented
    }});
    
'''
        else:
            code += f'''    test('example test case', () => {{
        // Arrange
        
        // Act
        
        // Assert
        expect(true).toBe(true); // Test not implemented
    }});
'''
        
        code += '});\n'
        return code
    
    def _generate_junit_template(self, test_name: str, class_name: str, methods: List[str]) -> str:
        """Generate JUnit (Java) template."""
        test_class_name = f"Test{class_name or test_name.replace('_', '').title()}"
        code = f'''import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Test class for {class_name or test_name}
 */
public class {test_class_name} {{
    
    @BeforeEach
    public void setUp() {{
        // Setup code here
    }}
    
    @AfterEach
    public void tearDown() {{
        // Teardown code here
    }}
    
'''
        
        if methods:
            for method in methods:
                code += f'''    @Test
    public void test{method.replace('_', '').title()}() {{
        // Arrange
        
        // Act
        
        // Assert
        fail("Test not implemented");
    }}
    
'''
        else:
            code += f'''    @Test
    public void testExample() {{
        // Arrange
        
        // Act
        
        // Assert
        fail("Test not implemented");
    }}
'''
        
        code += '}\n'
        return code


def main():
    """Main entry point for the test generator."""
    parser = argparse.ArgumentParser(
        description='Generate test automation code templates',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python test_generator.py --framework pytest --name user_service --class UserService --methods create,update,delete
  python test_generator.py --framework junit --name calculator --class Calculator --output tests/
  python test_generator.py --framework jest --name api_client --methods get,post,put
        '''
    )
    
    parser.add_argument(
        '--framework', '-f',
        required=True,
        choices=['pytest', 'unittest', 'jest', 'junit'],
        help='Testing framework to generate code for'
    )
    
    parser.add_argument(
        '--name', '-n',
        required=True,
        help='Name of the test (used for file/class naming)'
    )
    
    parser.add_argument(
        '--class', '-c',
        dest='class_name',
        help='Name of the class being tested (optional)'
    )
    
    parser.add_argument(
        '--methods', '-m',
        help='Comma-separated list of methods to generate tests for (optional)'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='Output directory for generated test file (optional, prints to stdout if not provided)'
    )
    
    args = parser.parse_args()
    
    # Parse methods list
    methods = []
    if args.methods:
        methods = [m.strip() for m in args.methods.split(',')]
    
    # Generate test code
    generator = TestGenerator()
    try:
        test_code = generator.generate(
            args.framework,
            args.name,
            args.class_name,
            methods
        )
        
        # Output to file or stdout
        if args.output:
            # Determine file extension
            extensions = {
                'pytest': 'py',
                'unittest': 'py',
                'jest': 'test.js',
                'junit': 'java'
            }
            ext = extensions[args.framework]
            
            # Create output directory if it doesn't exist
            os.makedirs(args.output, exist_ok=True)
            
            # Generate filename
            if args.framework in ['pytest', 'unittest']:
                filename = f"test_{args.name}.{ext}"
            elif args.framework == 'jest':
                filename = f"{args.name}.{ext}"
            else:  # junit
                class_name = f"Test{args.class_name or args.name.replace('_', '').title()}"
                filename = f"{class_name}.{ext}"
            
            filepath = os.path.join(args.output, filename)
            
            with open(filepath, 'w') as f:
                f.write(test_code)
            
            print(f"✓ Test file generated: {filepath}")
        else:
            print(test_code)
    
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())

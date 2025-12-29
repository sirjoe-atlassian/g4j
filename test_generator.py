#!/usr/bin/env python3
"""
Test Automation Code Generator

This module provides functionality to automatically generate test code
based on source code analysis and templates.
"""

import ast
import inspect
from typing import List, Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class FunctionInfo:
    """Information about a function to generate tests for."""
    name: str
    args: List[str]
    docstring: Optional[str]
    return_annotation: Optional[str]


class TestCodeGenerator:
    """Generates automated test code for Python functions and classes."""
    
    def __init__(self, framework: str = "pytest"):
        """
        Initialize the test generator.
        
        Args:
            framework: Testing framework to use ('pytest' or 'unittest')
        """
        self.framework = framework
    
    def parse_source_file(self, filepath: str) -> List[FunctionInfo]:
        """
        Parse a Python source file and extract function information.
        
        Args:
            filepath: Path to the Python source file
            
        Returns:
            List of FunctionInfo objects
        """
        with open(filepath, 'r') as f:
            source = f.read()
        
        tree = ast.parse(source)
        functions = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Skip private functions
                if node.name.startswith('_') and not node.name.startswith('__'):
                    continue
                    
                args = [arg.arg for arg in node.args.args if arg.arg != 'self']
                docstring = ast.get_docstring(node)
                return_annotation = None
                
                if node.returns:
                    return_annotation = ast.unparse(node.returns)
                
                functions.append(FunctionInfo(
                    name=node.name,
                    args=args,
                    docstring=docstring,
                    return_annotation=return_annotation
                ))
        
        return functions
    
    def generate_pytest_test(self, func_info: FunctionInfo, module_name: str) -> str:
        """
        Generate a pytest test for a function.
        
        Args:
            func_info: Information about the function
            module_name: Name of the module containing the function
            
        Returns:
            Generated test code as a string
        """
        test_code = f"""
def test_{func_info.name}():
    \"\"\"Test for {func_info.name}.\"\"\"
    # TODO: Implement test for {func_info.name}
    # Function signature: {func_info.name}({', '.join(func_info.args)})
"""
        
        if func_info.docstring:
            test_code += f"    # Description: {func_info.docstring.split(chr(10))[0]}\n"
        
        test_code += f"""    
    # Arrange
    # TODO: Set up test data and expected values
    
    # Act
    # result = {module_name}.{func_info.name}(...)
    
    # Assert
    # assert result == expected_value
    pass
"""
        return test_code
    
    def generate_unittest_test(self, func_info: FunctionInfo, module_name: str) -> str:
        """
        Generate a unittest test for a function.
        
        Args:
            func_info: Information about the function
            module_name: Name of the module containing the function
            
        Returns:
            Generated test code as a string
        """
        class_name = ''.join(word.capitalize() for word in func_info.name.split('_'))
        test_code = f"""
    def test_{func_info.name}(self):
        \"\"\"Test for {func_info.name}.\"\"\"
        # TODO: Implement test for {func_info.name}
        # Function signature: {func_info.name}({', '.join(func_info.args)})
"""
        
        if func_info.docstring:
            test_code += f"        # Description: {func_info.docstring.split(chr(10))[0]}\n"
        
        test_code += f"""        
        # Arrange
        # TODO: Set up test data and expected values
        
        # Act
        # result = {module_name}.{func_info.name}(...)
        
        # Assert
        # self.assertEqual(result, expected_value)
        pass
"""
        return test_code
    
    def generate_test_file(self, source_filepath: str, output_filepath: str) -> None:
        """
        Generate a complete test file for a source file.
        
        Args:
            source_filepath: Path to the source file
            output_filepath: Path to write the test file
        """
        functions = self.parse_source_file(source_filepath)
        module_name = source_filepath.replace('.py', '').replace('/', '.').replace('\\', '.')
        
        if self.framework == "pytest":
            test_content = self._generate_pytest_file(functions, module_name, source_filepath)
        else:
            test_content = self._generate_unittest_file(functions, module_name, source_filepath)
        
        with open(output_filepath, 'w') as f:
            f.write(test_content)
        
        print(f"Generated test file: {output_filepath}")
        print(f"Number of test stubs created: {len(functions)}")
    
    def _generate_pytest_file(self, functions: List[FunctionInfo], module_name: str, source_file: str) -> str:
        """Generate a complete pytest test file."""
        content = f'''"""
Automated tests for {source_file}

This file was auto-generated by TestCodeGenerator.
Please fill in the TODO sections with actual test implementations.
"""

import pytest
# TODO: Import the module to test
# import {module_name}

'''
        
        for func_info in functions:
            content += self.generate_pytest_test(func_info, module_name)
        
        return content
    
    def _generate_unittest_file(self, functions: List[FunctionInfo], module_name: str, source_file: str) -> str:
        """Generate a complete unittest test file."""
        content = f'''"""
Automated tests for {source_file}

This file was auto-generated by TestCodeGenerator.
Please fill in the TODO sections with actual test implementations.
"""

import unittest
# TODO: Import the module to test
# import {module_name}


class TestModule(unittest.TestCase):
    """Test cases for {source_file}."""
    
    def setUp(self):
        """Set up test fixtures."""
        pass
    
    def tearDown(self):
        """Clean up after tests."""
        pass
'''
        
        for func_info in functions:
            content += self.generate_unittest_test(func_info, module_name)
        
        content += '''

if __name__ == '__main__':
    unittest.main()
'''
        return content


def main():
    """Main entry point for the test generator CLI."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate automated test code from source files')
    parser.add_argument('source_file', help='Path to the source file to generate tests for')
    parser.add_argument('-o', '--output', help='Output test file path', default=None)
    parser.add_argument('-f', '--framework', choices=['pytest', 'unittest'], 
                       default='pytest', help='Testing framework (default: pytest)')
    
    args = parser.parse_args()
    
    if args.output is None:
        # Generate default output filename
        if args.source_file.endswith('.py'):
            args.output = args.source_file.replace('.py', '_test.py')
        else:
            args.output = args.source_file + '_test.py'
    
    generator = TestCodeGenerator(framework=args.framework)
    generator.generate_test_file(args.source_file, args.output)


if __name__ == '__main__':
    main()

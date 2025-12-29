#!/usr/bin/env python3
"""
Test Automation Code Generator

This module provides functionality to automatically generate test code
for Python functions and classes.
"""

import ast
import inspect
import re
from typing import List, Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class TestCase:
    """Represents a single test case."""
    function_name: str
    test_name: str
    test_code: str
    description: str


class TestCodeGenerator:
    """Generates automated test code for Python functions and classes."""
    
    def __init__(self, framework: str = "pytest"):
        """
        Initialize the test code generator.
        
        Args:
            framework: Testing framework to use ('pytest' or 'unittest')
        """
        self.framework = framework.lower()
        if self.framework not in ["pytest", "unittest"]:
            raise ValueError("Framework must be 'pytest' or 'unittest'")
    
    def generate_test_for_function(self, func) -> str:
        """
        Generate test code for a given function.
        
        Args:
            func: The function to generate tests for
            
        Returns:
            String containing the generated test code
        """
        func_name = func.__name__
        sig = inspect.signature(func)
        params = list(sig.parameters.keys())
        
        if self.framework == "pytest":
            return self._generate_pytest_function(func_name, params)
        else:
            return self._generate_unittest_function(func_name, params)
    
    def generate_test_from_source(self, source_code: str, module_name: str = "module") -> str:
        """
        Generate test code from source code string.
        
        Args:
            source_code: Python source code as a string
            module_name: Name of the module being tested
            
        Returns:
            String containing the generated test code
        """
        try:
            tree = ast.parse(source_code)
        except SyntaxError as e:
            raise ValueError(f"Invalid Python source code: {e}")
        
        functions = []
        classes = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if not node.name.startswith('_'):  # Skip private functions
                    functions.append(self._extract_function_info(node))
            elif isinstance(node, ast.ClassDef):
                classes.append(self._extract_class_info(node))
        
        if self.framework == "pytest":
            return self._generate_pytest_file(functions, classes, module_name)
        else:
            return self._generate_unittest_file(functions, classes, module_name)
    
    def _extract_function_info(self, node: ast.FunctionDef) -> Dict[str, Any]:
        """Extract information from a function AST node."""
        return {
            'name': node.name,
            'args': [arg.arg for arg in node.args.args if arg.arg != 'self'],
            'docstring': ast.get_docstring(node) or '',
            'returns': node.returns is not None
        }
    
    def _extract_class_info(self, node: ast.ClassDef) -> Dict[str, Any]:
        """Extract information from a class AST node."""
        methods = []
        for item in node.body:
            if isinstance(item, ast.FunctionDef) and not item.name.startswith('_'):
                methods.append(self._extract_function_info(item))
        
        return {
            'name': node.name,
            'methods': methods,
            'docstring': ast.get_docstring(node) or ''
        }
    
    def _generate_pytest_function(self, func_name: str, params: List[str]) -> str:
        """Generate pytest test code for a function."""
        param_setup = self._generate_sample_params(params, indent_level=1)
        test_code = f"""
def test_{func_name}_basic():
    \"\"\"Test basic functionality of {func_name}.\"\"\"
    # Arrange
    {param_setup}
    
    # Act
    result = {func_name}({', '.join(params)})
    
    # Assert
    assert result is not None
    # TODO: Add specific assertions


def test_{func_name}_edge_cases():
    \"\"\"Test edge cases for {func_name}.\"\"\"
    # TODO: Implement edge case tests
    pass


def test_{func_name}_invalid_input():
    \"\"\"Test {func_name} with invalid input.\"\"\"
    # TODO: Test error handling
    pass
"""
        return test_code
    
    def _generate_unittest_function(self, func_name: str, params: List[str]) -> str:
        """Generate unittest test code for a function."""
        class_name = ''.join(word.capitalize() for word in func_name.split('_'))
        param_setup = self._generate_sample_params(params, indent_level=2)
        test_code = f"""
class Test{class_name}(unittest.TestCase):
    \"\"\"Test cases for {func_name} function.\"\"\"
    
    def test_{func_name}_basic(self):
        \"\"\"Test basic functionality of {func_name}.\"\"\"
        # Arrange
        {param_setup}
        
        # Act
        result = {func_name}({', '.join(params)})
        
        # Assert
        self.assertIsNotNone(result)
        # TODO: Add specific assertions
    
    def test_{func_name}_edge_cases(self):
        \"\"\"Test edge cases for {func_name}.\"\"\"
        # TODO: Implement edge case tests
        pass
    
    def test_{func_name}_invalid_input(self):
        \"\"\"Test {func_name} with invalid input.\"\"\"
        # TODO: Test error handling
        pass
"""
        return test_code
    
    def _generate_pytest_file(self, functions: List[Dict], classes: List[Dict], module_name: str) -> str:
        """Generate complete pytest file."""
        imports = f"""import pytest
from {module_name} import *


"""
        
        test_code = imports
        
        # Generate tests for standalone functions
        for func in functions:
            test_code += self._generate_pytest_function(func['name'], func['args'])
            test_code += "\n"
        
        # Generate tests for class methods
        for cls in classes:
            test_code += f"\n# Tests for {cls['name']} class\n"
            test_code += f"""
class Test{cls['name']}:
    \"\"\"Test suite for {cls['name']} class.\"\"\"
    
    @pytest.fixture
    def instance(self):
        \"\"\"Create a {cls['name']} instance for testing.\"\"\"
        return {cls['name']}()
    
"""
            for method in cls['methods']:
                method_params = self._generate_sample_params(method['args'], indent_level=2)
                test_code += f"""
    def test_{method['name']}(self, instance):
        \"\"\"Test {method['name']} method.\"\"\"
        # Arrange
        {method_params}
        
        # Act
        result = instance.{method['name']}({', '.join(method['args'])})
        
        # Assert
        assert result is not None
        # TODO: Add specific assertions
"""
        
        return test_code
    
    def _generate_unittest_file(self, functions: List[Dict], classes: List[Dict], module_name: str) -> str:
        """Generate complete unittest file."""
        imports = f"""import unittest
from {module_name} import *


"""
        
        test_code = imports
        
        # Generate tests for standalone functions
        for func in functions:
            test_code += self._generate_unittest_function(func['name'], func['args'])
            test_code += "\n"
        
        # Generate tests for class methods
        for cls in classes:
            test_code += f"\n# Tests for {cls['name']} class\n"
            test_code += f"""
class Test{cls['name']}(unittest.TestCase):
    \"\"\"Test suite for {cls['name']} class.\"\"\"
    
    def setUp(self):
        \"\"\"Set up test fixtures.\"\"\"
        self.instance = {cls['name']}()
    
"""
            for method in cls['methods']:
                method_params = self._generate_sample_params(method['args'], indent_level=2)
                test_code += f"""
    def test_{method['name']}(self):
        \"\"\"Test {method['name']} method.\"\"\"
        # Arrange
        {method_params}
        
        # Act
        result = self.instance.{method['name']}({', '.join(method['args'])})
        
        # Assert
        self.assertIsNotNone(result)
        # TODO: Add specific assertions
"""
        
        test_code += """

if __name__ == '__main__':
    unittest.main()
"""
        
        return test_code
    
    def _generate_sample_params(self, params: List[str], indent_level: int = 2) -> str:
        """Generate sample parameter assignments."""
        if not params:
            return "# No parameters required"
        
        indent = "    " * indent_level
        assignments = []
        for param in params:
            # Try to infer type from parameter name
            if any(word in param.lower() for word in ['count', 'num', 'size', 'index']):
                assignments.append(f"{param} = 1")
            elif any(word in param.lower() for word in ['name', 'text', 'str', 'msg']):
                assignments.append(f'{param} = "test"')
            elif any(word in param.lower() for word in ['list', 'items', 'array']):
                assignments.append(f'{param} = []')
            elif any(word in param.lower() for word in ['dict', 'map', 'config']):
                assignments.append(f'{param} = {{}}')
            elif any(word in param.lower() for word in ['flag', 'is_', 'has_', 'enabled']):
                assignments.append(f'{param} = True')
            else:
                assignments.append(f'{param} = None  # TODO: Set appropriate value')
        
        return f'\n{indent}'.join(assignments)


def generate_test_file(source_file: str, output_file: str, framework: str = "pytest"):
    """
    Generate a test file from a source code file.
    
    Args:
        source_file: Path to the source Python file
        output_file: Path where the test file should be written
        framework: Testing framework to use ('pytest' or 'unittest')
    """
    with open(source_file, 'r') as f:
        source_code = f.read()
    
    module_name = source_file.replace('.py', '').replace('/', '.')
    if module_name.startswith('.'):
        module_name = module_name[1:]
    
    generator = TestCodeGenerator(framework=framework)
    test_code = generator.generate_test_from_source(source_code, module_name)
    
    with open(output_file, 'w') as f:
        f.write(test_code)
    
    print(f"Generated test file: {output_file}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python test_generator.py <source_file> [output_file] [framework]")
        print("  source_file: Python source file to generate tests for")
        print("  output_file: Output test file (default: test_<source_file>)")
        print("  framework: 'pytest' or 'unittest' (default: pytest)")
        sys.exit(1)
    
    source = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else f"test_{source}"
    framework = sys.argv[3] if len(sys.argv) > 3 else "pytest"
    
    generate_test_file(source, output, framework)

"""
Test Automation Code Generator

This module provides functionality to automatically generate test code
based on various inputs and templates.
"""

import re
import inspect
from typing import List, Dict, Any, Callable, Optional


class TestCodeGenerator:
    """
    A class to generate automated test code for functions and classes.
    """
    
    def __init__(self, test_framework: str = "pytest"):
        """
        Initialize the test code generator.
        
        Args:
            test_framework: The testing framework to use (pytest, unittest, etc.)
        """
        self.test_framework = test_framework
        self.generated_tests = []
    
    def generate_function_test(self, 
                               func: Callable, 
                               test_cases: List[Dict[str, Any]]) -> str:
        """
        Generate test code for a given function.
        
        Args:
            func: The function to generate tests for
            test_cases: List of test cases with 'inputs' and 'expected' keys
            
        Returns:
            str: Generated test code
        """
        func_name = func.__name__
        test_code = []
        
        if self.test_framework == "pytest":
            test_code.append(f"import pytest\n")
            test_code.append(f"from {func.__module__} import {func_name}\n\n")
            
            for idx, test_case in enumerate(test_cases):
                test_code.append(f"def test_{func_name}_{idx + 1}():\n")
                
                # Generate input parameters
                inputs = test_case.get('inputs', {})
                expected = test_case.get('expected')
                
                # Build function call
                if isinstance(inputs, dict):
                    params = ', '.join([f"{k}={repr(v)}" for k, v in inputs.items()])
                else:
                    params = repr(inputs)
                
                test_code.append(f"    result = {func_name}({params})\n")
                test_code.append(f"    assert result == {repr(expected)}\n\n")
        
        elif self.test_framework == "unittest":
            test_code.append(f"import unittest\n")
            test_code.append(f"from {func.__module__} import {func_name}\n\n")
            test_code.append(f"class Test{func_name.title()}(unittest.TestCase):\n\n")
            
            for idx, test_case in enumerate(test_cases):
                test_code.append(f"    def test_{func_name}_{idx + 1}(self):\n")
                
                inputs = test_case.get('inputs', {})
                expected = test_case.get('expected')
                
                if isinstance(inputs, dict):
                    params = ', '.join([f"{k}={repr(v)}" for k, v in inputs.items()])
                else:
                    params = repr(inputs)
                
                test_code.append(f"        result = {func_name}({params})\n")
                test_code.append(f"        self.assertEqual(result, {repr(expected)})\n\n")
        
        generated = ''.join(test_code)
        self.generated_tests.append(generated)
        return generated
    
    def generate_class_test(self, 
                            cls: type, 
                            method_tests: Dict[str, List[Dict[str, Any]]]) -> str:
        """
        Generate test code for a class and its methods.
        
        Args:
            cls: The class to generate tests for
            method_tests: Dictionary mapping method names to test cases
            
        Returns:
            str: Generated test code
        """
        class_name = cls.__name__
        test_code = []
        
        if self.test_framework == "pytest":
            test_code.append(f"import pytest\n")
            test_code.append(f"from {cls.__module__} import {class_name}\n\n")
            
            for method_name, test_cases in method_tests.items():
                for idx, test_case in enumerate(test_cases):
                    test_code.append(f"def test_{class_name}_{method_name}_{idx + 1}():\n")
                    
                    # Generate instance creation
                    init_params = test_case.get('init_params', {})
                    if init_params:
                        params = ', '.join([f"{k}={repr(v)}" for k, v in init_params.items()])
                        test_code.append(f"    obj = {class_name}({params})\n")
                    else:
                        test_code.append(f"    obj = {class_name}()\n")
                    
                    # Generate method call
                    inputs = test_case.get('inputs', {})
                    expected = test_case.get('expected')
                    
                    if isinstance(inputs, dict):
                        params = ', '.join([f"{k}={repr(v)}" for k, v in inputs.items()])
                    else:
                        params = repr(inputs) if inputs else ''
                    
                    test_code.append(f"    result = obj.{method_name}({params})\n")
                    test_code.append(f"    assert result == {repr(expected)}\n\n")
        
        elif self.test_framework == "unittest":
            test_code.append(f"import unittest\n")
            test_code.append(f"from {cls.__module__} import {class_name}\n\n")
            test_code.append(f"class Test{class_name}(unittest.TestCase):\n\n")
            
            for method_name, test_cases in method_tests.items():
                for idx, test_case in enumerate(test_cases):
                    test_code.append(f"    def test_{method_name}_{idx + 1}(self):\n")
                    
                    init_params = test_case.get('init_params', {})
                    if init_params:
                        params = ', '.join([f"{k}={repr(v)}" for k, v in init_params.items()])
                        test_code.append(f"        obj = {class_name}({params})\n")
                    else:
                        test_code.append(f"        obj = {class_name}()\n")
                    
                    inputs = test_case.get('inputs', {})
                    expected = test_case.get('expected')
                    
                    if isinstance(inputs, dict):
                        params = ', '.join([f"{k}={repr(v)}" for k, v in inputs.items()])
                    else:
                        params = repr(inputs) if inputs else ''
                    
                    test_code.append(f"        result = obj.{method_name}({params})\n")
                    test_code.append(f"        self.assertEqual(result, {repr(expected)})\n\n")
        
        generated = ''.join(test_code)
        self.generated_tests.append(generated)
        return generated
    
    def generate_api_test(self, 
                          endpoint: str, 
                          method: str,
                          test_cases: List[Dict[str, Any]]) -> str:
        """
        Generate test code for API endpoints.
        
        Args:
            endpoint: The API endpoint to test
            method: HTTP method (GET, POST, etc.)
            test_cases: List of test cases with request data and expected responses
            
        Returns:
            str: Generated test code
        """
        safe_endpoint = re.sub(r'[^a-zA-Z0-9_]', '_', endpoint)
        test_code = []
        
        if self.test_framework == "pytest":
            test_code.append(f"import pytest\n")
            test_code.append(f"import requests\n\n")
            
            for idx, test_case in enumerate(test_cases):
                test_code.append(f"def test_api_{method.lower()}_{safe_endpoint}_{idx + 1}():\n")
                test_code.append(f"    url = '{endpoint}'\n")
                
                headers = test_case.get('headers', {})
                data = test_case.get('data', {})
                expected_status = test_case.get('expected_status', 200)
                expected_response = test_case.get('expected_response')
                
                if headers:
                    test_code.append(f"    headers = {repr(headers)}\n")
                if data:
                    test_code.append(f"    data = {repr(data)}\n")
                
                # Generate request call
                request_params = []
                if headers:
                    request_params.append("headers=headers")
                if data:
                    if method.upper() in ['POST', 'PUT', 'PATCH']:
                        request_params.append("json=data")
                    else:
                        request_params.append("params=data")
                
                params_str = ', '.join(request_params)
                test_code.append(f"    response = requests.{method.lower()}(url, {params_str})\n")
                test_code.append(f"    assert response.status_code == {expected_status}\n")
                
                if expected_response:
                    test_code.append(f"    assert response.json() == {repr(expected_response)}\n")
                
                test_code.append("\n")
        
        generated = ''.join(test_code)
        self.generated_tests.append(generated)
        return generated
    
    def save_tests(self, filepath: str):
        """
        Save all generated tests to a file.
        
        Args:
            filepath: Path to save the test file
        """
        with open(filepath, 'w') as f:
            for test in self.generated_tests:
                f.write(test)
                f.write("\n")
    
    def clear_tests(self):
        """Clear all generated tests."""
        self.generated_tests = []


# Example usage
if __name__ == "__main__":
    # Example function to test
    def add_numbers(a: int, b: int) -> int:
        """Add two numbers together."""
        return a + b
    
    # Create generator
    generator = TestCodeGenerator(test_framework="pytest")
    
    # Generate tests for the function
    test_cases = [
        {'inputs': {'a': 1, 'b': 2}, 'expected': 3},
        {'inputs': {'a': 0, 'b': 0}, 'expected': 0},
        {'inputs': {'a': -1, 'b': 1}, 'expected': 0},
        {'inputs': {'a': 100, 'b': 200}, 'expected': 300},
    ]
    
    generated_code = generator.generate_function_test(add_numbers, test_cases)
    print("Generated Test Code:")
    print("=" * 50)
    print(generated_code)
    
    # Generate API tests
    api_test_cases = [
        {
            'headers': {'Content-Type': 'application/json'},
            'data': {'name': 'John', 'age': 30},
            'expected_status': 201,
            'expected_response': {'id': 1, 'name': 'John', 'age': 30}
        }
    ]
    
    api_test_code = generator.generate_api_test('/api/users', 'POST', api_test_cases)
    print("\nGenerated API Test Code:")
    print("=" * 50)
    print(api_test_code)

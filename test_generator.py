#!/usr/bin/env python3
"""
Test Automation Code Generator

This module provides functionality to generate test automation code
for various testing frameworks and languages.
"""

import os
import json
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum


class TestFramework(Enum):
    """Supported test frameworks"""
    PYTEST = "pytest"
    UNITTEST = "unittest"
    JUNIT = "junit"
    JEST = "jest"
    MOCHA = "mocha"


class Language(Enum):
    """Supported programming languages"""
    PYTHON = "python"
    JAVA = "java"
    JAVASCRIPT = "javascript"
    TYPESCRIPT = "typescript"


@dataclass
class TestCase:
    """Represents a test case"""
    name: str
    description: str
    setup: Optional[str] = None
    teardown: Optional[str] = None
    assertions: List[str] = None
    test_data: Optional[Dict] = None

    def __post_init__(self):
        if self.assertions is None:
            self.assertions = []
        if self.test_data is None:
            self.test_data = {}


class TestGenerator:
    """Base class for test code generation"""
    
    def __init__(self, framework: TestFramework, language: Language):
        self.framework = framework
        self.language = language
    
    def generate_test_suite(self, test_cases: List[TestCase], class_name: str = "TestSuite") -> str:
        """Generate a complete test suite from test cases"""
        raise NotImplementedError("Subclasses must implement generate_test_suite")
    
    def generate_test_case(self, test_case: TestCase) -> str:
        """Generate code for a single test case"""
        raise NotImplementedError("Subclasses must implement generate_test_case")


class PytestGenerator(TestGenerator):
    """Generator for pytest test cases"""
    
    def __init__(self):
        super().__init__(TestFramework.PYTEST, Language.PYTHON)
    
    def generate_test_suite(self, test_cases: List[TestCase], class_name: str = "TestSuite") -> str:
        """Generate pytest test suite"""
        imports = "import pytest\n\n"
        
        class_code = f"class {class_name}:\n"
        class_code += '    """Generated test suite"""\n\n'
        
        for test_case in test_cases:
            class_code += self.generate_test_case(test_case)
            class_code += "\n"
        
        return imports + class_code
    
    def generate_test_case(self, test_case: TestCase) -> str:
        """Generate pytest test case"""
        test_code = f"    def test_{test_case.name}(self):\n"
        test_code += f'        """{test_case.description}"""\n'
        
        if test_case.setup:
            test_code += f"        # Setup\n"
            test_code += f"        {test_case.setup}\n\n"
        
        test_code += f"        # Test execution\n"
        for assertion in test_case.assertions:
            test_code += f"        {assertion}\n"
        
        if test_case.teardown:
            test_code += f"\n        # Teardown\n"
            test_code += f"        {test_case.teardown}\n"
        
        return test_code


class UnittestGenerator(TestGenerator):
    """Generator for unittest test cases"""
    
    def __init__(self):
        super().__init__(TestFramework.UNITTEST, Language.PYTHON)
    
    def generate_test_suite(self, test_cases: List[TestCase], class_name: str = "TestSuite") -> str:
        """Generate unittest test suite"""
        imports = "import unittest\n\n"
        
        class_code = f"class {class_name}(unittest.TestCase):\n"
        class_code += '    """Generated test suite"""\n\n'
        
        for test_case in test_cases:
            class_code += self.generate_test_case(test_case)
            class_code += "\n"
        
        class_code += '\nif __name__ == "__main__":\n'
        class_code += "    unittest.main()\n"
        
        return imports + class_code
    
    def generate_test_case(self, test_case: TestCase) -> str:
        """Generate unittest test case"""
        test_code = f"    def test_{test_case.name}(self):\n"
        test_code += f'        """{test_case.description}"""\n'
        
        if test_case.setup:
            test_code += f"        # Setup\n"
            test_code += f"        {test_case.setup}\n\n"
        
        test_code += f"        # Test execution\n"
        for assertion in test_case.assertions:
            test_code += f"        {assertion}\n"
        
        if test_case.teardown:
            test_code += f"\n        # Teardown\n"
            test_code += f"        {test_case.teardown}\n"
        
        return test_code


class JUnitGenerator(TestGenerator):
    """Generator for JUnit test cases"""
    
    def __init__(self):
        super().__init__(TestFramework.JUNIT, Language.JAVA)
    
    def generate_test_suite(self, test_cases: List[TestCase], class_name: str = "TestSuite") -> str:
        """Generate JUnit test suite"""
        imports = "import org.junit.jupiter.api.Test;\n"
        imports += "import static org.junit.jupiter.api.Assertions.*;\n\n"
        
        class_code = f"public class {class_name} {{\n\n"
        
        for test_case in test_cases:
            class_code += self.generate_test_case(test_case)
            class_code += "\n"
        
        class_code += "}\n"
        
        return imports + class_code
    
    def generate_test_case(self, test_case: TestCase) -> str:
        """Generate JUnit test case"""
        test_code = "    @Test\n"
        test_code += f"    public void test{test_case.name.capitalize()}() {{\n"
        test_code += f"        // {test_case.description}\n"
        
        if test_case.setup:
            test_code += f"        // Setup\n"
            test_code += f"        {test_case.setup}\n\n"
        
        test_code += f"        // Test execution\n"
        for assertion in test_case.assertions:
            test_code += f"        {assertion}\n"
        
        if test_case.teardown:
            test_code += f"\n        // Teardown\n"
            test_code += f"        {test_case.teardown}\n"
        
        test_code += "    }\n"
        
        return test_code


class JestGenerator(TestGenerator):
    """Generator for Jest test cases"""
    
    def __init__(self):
        super().__init__(TestFramework.JEST, Language.JAVASCRIPT)
    
    def generate_test_suite(self, test_cases: List[TestCase], class_name: str = "TestSuite") -> str:
        """Generate Jest test suite"""
        suite_code = f"describe('{class_name}', () => {{\n\n"
        
        for test_case in test_cases:
            suite_code += self.generate_test_case(test_case)
            suite_code += "\n"
        
        suite_code += "});\n"
        
        return suite_code
    
    def generate_test_case(self, test_case: TestCase) -> str:
        """Generate Jest test case"""
        test_code = f"  test('{test_case.name}', () => {{\n"
        test_code += f"    // {test_case.description}\n"
        
        if test_case.setup:
            test_code += f"    // Setup\n"
            test_code += f"    {test_case.setup}\n\n"
        
        test_code += f"    // Test execution\n"
        for assertion in test_case.assertions:
            test_code += f"    {assertion}\n"
        
        if test_case.teardown:
            test_code += f"\n    // Teardown\n"
            test_code += f"    {test_case.teardown}\n"
        
        test_code += "  });\n"
        
        return test_code


def create_generator(framework: TestFramework) -> TestGenerator:
    """Factory function to create appropriate test generator"""
    generators = {
        TestFramework.PYTEST: PytestGenerator,
        TestFramework.UNITTEST: UnittestGenerator,
        TestFramework.JUNIT: JUnitGenerator,
        TestFramework.JEST: JestGenerator,
    }
    
    generator_class = generators.get(framework)
    if not generator_class:
        raise ValueError(f"Unsupported framework: {framework}")
    
    return generator_class()


def generate_from_json(json_file: str, framework: TestFramework, output_file: str):
    """Generate test code from JSON specification"""
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    test_cases = []
    for tc_data in data.get('test_cases', []):
        test_case = TestCase(
            name=tc_data['name'],
            description=tc_data.get('description', ''),
            setup=tc_data.get('setup'),
            teardown=tc_data.get('teardown'),
            assertions=tc_data.get('assertions', []),
            test_data=tc_data.get('test_data', {})
        )
        test_cases.append(test_case)
    
    generator = create_generator(framework)
    class_name = data.get('class_name', 'TestSuite')
    code = generator.generate_test_suite(test_cases, class_name)
    
    with open(output_file, 'w') as f:
        f.write(code)
    
    print(f"Generated test code in {output_file}")


def main():
    """Example usage"""
    # Example: Generate pytest tests
    test_cases = [
        TestCase(
            name="addition",
            description="Test addition operation",
            setup="calculator = Calculator()",
            assertions=[
                "result = calculator.add(2, 3)",
                "assert result == 5"
            ]
        ),
        TestCase(
            name="subtraction",
            description="Test subtraction operation",
            setup="calculator = Calculator()",
            assertions=[
                "result = calculator.subtract(10, 5)",
                "assert result == 5"
            ]
        ),
    ]
    
    generator = create_generator(TestFramework.PYTEST)
    code = generator.generate_test_suite(test_cases, "CalculatorTests")
    print(code)


if __name__ == "__main__":
    main()

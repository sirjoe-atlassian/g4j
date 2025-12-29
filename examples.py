#!/usr/bin/env python3
"""
Examples demonstrating the Test Automation Code Generator
"""

from test_automation_generator import TestGenerator, TestFramework, Language


def example_pytest():
    """Example: Generate pytest tests"""
    print("=" * 60)
    print("Example 1: Python pytest")
    print("=" * 60)
    
    generator = TestGenerator(TestFramework.PYTEST, Language.PYTHON)
    code = generator.generate_test_class("Calculator", ["add", "subtract", "multiply", "divide"])
    print(code)
    print("\n")


def example_unittest():
    """Example: Generate unittest tests"""
    print("=" * 60)
    print("Example 2: Python unittest")
    print("=" * 60)
    
    generator = TestGenerator(TestFramework.UNITTEST, Language.PYTHON)
    code = generator.generate_test_class("StringUtils", ["concat", "split", "trim"])
    print(code)
    print("\n")


def example_jest():
    """Example: Generate Jest tests for JavaScript"""
    print("=" * 60)
    print("Example 3: JavaScript Jest")
    print("=" * 60)
    
    generator = TestGenerator(TestFramework.JEST, Language.JAVASCRIPT)
    code = generator.generate_test_class("UserService", ["createUser", "updateUser", "deleteUser"])
    print(code)
    print("\n")


def example_mocha():
    """Example: Generate Mocha tests"""
    print("=" * 60)
    print("Example 4: JavaScript Mocha")
    print("=" * 60)
    
    generator = TestGenerator(TestFramework.MOCHA, Language.JAVASCRIPT)
    code = generator.generate_test_class("PaymentProcessor", ["processPayment", "refundPayment"])
    print(code)
    print("\n")


def example_typescript():
    """Example: Generate TypeScript Jest tests"""
    print("=" * 60)
    print("Example 5: TypeScript Jest")
    print("=" * 60)
    
    generator = TestGenerator(TestFramework.JEST, Language.TYPESCRIPT)
    code = generator.generate_test_class("AuthService", ["login", "logout", "validateToken"])
    print(code)
    print("\n")


def example_junit():
    """Example: Generate JUnit tests for Java"""
    print("=" * 60)
    print("Example 6: Java JUnit")
    print("=" * 60)
    
    generator = TestGenerator(TestFramework.JUNIT, Language.JAVA)
    code = generator.generate_test_class("DataProcessor", ["processData", "validateData", "transformData"])
    print(code)
    print("\n")


def example_test_suite():
    """Example: Generate multiple test files at once"""
    print("=" * 60)
    print("Example 7: Generate Multiple Test Files")
    print("=" * 60)
    
    generator = TestGenerator(TestFramework.PYTEST, Language.PYTHON)
    
    test_specs = [
        {"class_name": "Calculator", "methods": ["add", "subtract"]},
        {"class_name": "StringUtils", "methods": ["concat", "split"]},
        {"class_name": "FileHandler", "methods": ["read", "write", "delete"]},
    ]
    
    test_files = generator.generate_test_suite(test_specs)
    
    for filename, code in test_files.items():
        print(f"\n--- {filename} ---")
        print(code[:300] + "...\n")  # Print first 300 chars of each file


def main():
    """Run all examples"""
    print("\n")
    print("#" * 60)
    print("# Test Automation Code Generator - Examples")
    print("#" * 60)
    print("\n")
    
    example_pytest()
    example_unittest()
    example_jest()
    example_mocha()
    example_typescript()
    example_junit()
    example_test_suite()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == '__main__':
    main()

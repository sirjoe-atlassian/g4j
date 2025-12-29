#!/usr/bin/env python3
"""
Demo script showcasing the test automation code generator
"""

from test_generator import (
    TestCase,
    TestFramework,
    create_generator,
    generate_from_json
)


def demo_pytest_generation():
    """Demo: Generate pytest tests"""
    print("=" * 70)
    print("DEMO 1: Generating Pytest Tests")
    print("=" * 70)
    
    test_cases = [
        TestCase(
            name="string_concatenation",
            description="Test string concatenation",
            setup="str1 = 'Hello'\nstr2 = 'World'",
            assertions=[
                "result = str1 + ' ' + str2",
                "assert result == 'Hello World'"
            ]
        ),
        TestCase(
            name="list_operations",
            description="Test list append operation",
            setup="my_list = [1, 2, 3]",
            assertions=[
                "my_list.append(4)",
                "assert len(my_list) == 4",
                "assert my_list[-1] == 4"
            ]
        )
    ]
    
    generator = create_generator(TestFramework.PYTEST)
    code = generator.generate_test_suite(test_cases, "StringAndListTests")
    print(code)


def demo_unittest_generation():
    """Demo: Generate unittest tests"""
    print("\n" + "=" * 70)
    print("DEMO 2: Generating Unittest Tests")
    print("=" * 70)
    
    test_cases = [
        TestCase(
            name="dictionary_operations",
            description="Test dictionary get operation",
            setup="my_dict = {'key1': 'value1', 'key2': 'value2'}",
            assertions=[
                "result = my_dict.get('key1')",
                "self.assertEqual(result, 'value1')"
            ]
        )
    ]
    
    generator = create_generator(TestFramework.UNITTEST)
    code = generator.generate_test_suite(test_cases, "DictionaryTests")
    print(code)


def demo_junit_generation():
    """Demo: Generate JUnit tests"""
    print("\n" + "=" * 70)
    print("DEMO 3: Generating JUnit Tests")
    print("=" * 70)
    
    test_cases = [
        TestCase(
            name="string_comparison",
            description="Test string equality",
            setup='String expected = "Hello";',
            assertions=[
                'String actual = "Hello";',
                'assertEquals(expected, actual);'
            ]
        ),
        TestCase(
            name="null_check",
            description="Test null value handling",
            assertions=[
                'String value = null;',
                'assertNull(value);'
            ]
        )
    ]
    
    generator = create_generator(TestFramework.JUNIT)
    code = generator.generate_test_suite(test_cases, "JavaStringTests")
    print(code)


def demo_jest_generation():
    """Demo: Generate Jest tests"""
    print("\n" + "=" * 70)
    print("DEMO 4: Generating Jest Tests")
    print("=" * 70)
    
    test_cases = [
        TestCase(
            name="array operations",
            description="Test array push and length",
            setup="const arr = [1, 2, 3];",
            assertions=[
                "arr.push(4);",
                "expect(arr.length).toBe(4);",
                "expect(arr[3]).toBe(4);"
            ]
        ),
        TestCase(
            name="object properties",
            description="Test object property access",
            setup="const obj = { name: 'John', age: 30 };",
            assertions=[
                "expect(obj.name).toBe('John');",
                "expect(obj.age).toBe(30);"
            ]
        )
    ]
    
    generator = create_generator(TestFramework.JEST)
    code = generator.generate_test_suite(test_cases, "JavaScriptTests")
    print(code)


def demo_json_generation():
    """Demo: Generate tests from JSON file"""
    print("\n" + "=" * 70)
    print("DEMO 5: Generating Tests from JSON Specification")
    print("=" * 70)
    
    print("\nUsing test_spec_example.json to generate pytest tests...")
    
    try:
        generate_from_json(
            json_file='test_spec_example.json',
            framework=TestFramework.PYTEST,
            output_file='generated_calculator_tests.py'
        )
        
        print("\nGenerated file: generated_calculator_tests.py")
        print("\nContent preview:")
        print("-" * 70)
        
        with open('generated_calculator_tests.py', 'r') as f:
            content = f.read()
            # Show first 500 characters
            print(content[:500])
            if len(content) > 500:
                print("\n... (truncated)")
    except Exception as e:
        print(f"Error: {e}")


def demo_complex_scenario():
    """Demo: Complex test scenario with setup and teardown"""
    print("\n" + "=" * 70)
    print("DEMO 6: Complex Test Scenario with Setup/Teardown")
    print("=" * 70)
    
    test_cases = [
        TestCase(
            name="database_connection",
            description="Test database connection and query",
            setup="db = Database('test.db')\ndb.connect()",
            assertions=[
                "result = db.query('SELECT * FROM users')",
                "assert len(result) > 0",
                "assert 'id' in result[0]"
            ],
            teardown="db.disconnect()\ndb.cleanup()"
        ),
        TestCase(
            name="file_operations",
            description="Test file read and write",
            setup="file_path = 'test_file.txt'\nwith open(file_path, 'w') as f:\n    f.write('test data')",
            assertions=[
                "with open(file_path, 'r') as f:",
                "    content = f.read()",
                "assert content == 'test data'"
            ],
            teardown="import os\nos.remove(file_path)"
        )
    ]
    
    generator = create_generator(TestFramework.PYTEST)
    code = generator.generate_test_suite(test_cases, "IntegrationTests")
    print(code)


def main():
    """Run all demos"""
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 15 + "Test Automation Code Generator Demo" + " " * 17 + "║")
    print("╚" + "=" * 68 + "╝")
    print("\n")
    
    demo_pytest_generation()
    demo_unittest_generation()
    demo_junit_generation()
    demo_jest_generation()
    demo_json_generation()
    demo_complex_scenario()
    
    print("\n" + "=" * 70)
    print("Demo completed! Check the generated files and examples above.")
    print("=" * 70)
    print("\nFor more information, see test_automation_guide.md")


if __name__ == "__main__":
    main()

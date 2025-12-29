"""
Example test cases demonstrating the test automation framework.
"""

import unittest
from test_automation import TestCase, TestRunner, TestLogger, DataDrivenTest


class MathOperationsTest(TestCase):
    """Example test class for mathematical operations."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calculator_value = 0
    
    def test_addition_positive_numbers(self):
        """Test addition of positive numbers."""
        result = 10 + 5
        self.assertEqual(result, 15)
    
    def test_addition_negative_numbers(self):
        """Test addition of negative numbers."""
        result = -10 + (-5)
        self.assertEqual(result, -15)
    
    def test_subtraction(self):
        """Test subtraction operation."""
        result = 20 - 8
        self.assertEqual(result, 12)
    
    def test_multiplication(self):
        """Test multiplication operation."""
        result = 6 * 7
        self.assertEqual(result, 42)
    
    def test_division(self):
        """Test division operation."""
        result = 100 / 4
        self.assertEqual(result, 25.0)
    
    def test_division_by_zero(self):
        """Test division by zero raises exception."""
        with self.assertRaises(ZeroDivisionError):
            result = 10 / 0
    
    def test_between_assertion(self):
        """Test custom assertBetween method."""
        value = 50
        self.assertBetween(value, 0, 100)


class StringOperationsTest(TestCase):
    """Example test class for string operations."""
    
    def test_string_concatenation(self):
        """Test string concatenation."""
        result = "Hello" + " " + "World"
        self.assertEqual(result, "Hello World")
    
    def test_string_upper(self):
        """Test string upper method."""
        result = "hello".upper()
        self.assertEqual(result, "HELLO")
    
    def test_string_lower(self):
        """Test string lower method."""
        result = "WORLD".lower()
        self.assertEqual(result, "world")
    
    def test_string_contains(self):
        """Test string contains."""
        text = "The quick brown fox"
        self.assertIn("quick", text)
    
    def test_string_starts_with(self):
        """Test string starts with."""
        text = "Hello World"
        self.assertTrue(text.startswith("Hello"))
    
    def test_string_ends_with(self):
        """Test string ends with."""
        text = "Hello World"
        self.assertTrue(text.endswith("World"))


class ListOperationsTest(TestCase):
    """Example test class for list operations."""
    
    def test_list_append(self):
        """Test list append operation."""
        my_list = [1, 2, 3]
        my_list.append(4)
        self.assertEqual(my_list, [1, 2, 3, 4])
    
    def test_list_extend(self):
        """Test list extend operation."""
        my_list = [1, 2]
        my_list.extend([3, 4, 5])
        self.assertEqual(my_list, [1, 2, 3, 4, 5])
    
    def test_list_remove(self):
        """Test list remove operation."""
        my_list = [1, 2, 3, 4]
        my_list.remove(3)
        self.assertEqual(my_list, [1, 2, 4])
    
    def test_list_length(self):
        """Test list length."""
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(len(my_list), 5)
    
    def test_list_index(self):
        """Test list index access."""
        my_list = [10, 20, 30, 40]
        self.assertEqual(my_list[2], 30)


class DictionaryOperationsTest(TestCase):
    """Example test class for dictionary operations."""
    
    def test_dict_key_access(self):
        """Test dictionary key access."""
        my_dict = {"name": "John", "age": 30}
        self.assertEqual(my_dict["name"], "John")
    
    def test_dict_contains_key(self):
        """Test custom assertContainsKey method."""
        my_dict = {"name": "John", "age": 30, "city": "New York"}
        self.assertContainsKey(my_dict, "age")
    
    def test_dict_get_method(self):
        """Test dictionary get method."""
        my_dict = {"name": "John"}
        self.assertEqual(my_dict.get("name"), "John")
        self.assertIsNone(my_dict.get("nonexistent"))
    
    def test_dict_keys(self):
        """Test dictionary keys."""
        my_dict = {"a": 1, "b": 2, "c": 3}
        keys = list(my_dict.keys())
        self.assertEqual(sorted(keys), ["a", "b", "c"])
    
    def test_dict_values(self):
        """Test dictionary values."""
        my_dict = {"a": 1, "b": 2, "c": 3}
        values = list(my_dict.values())
        self.assertEqual(sorted(values), [1, 2, 3])


def run_all_tests():
    """Run all test suites."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(MathOperationsTest))
    suite.addTests(loader.loadTestsFromTestCase(StringOperationsTest))
    suite.addTests(loader.loadTestsFromTestCase(ListOperationsTest))
    suite.addTests(loader.loadTestsFromTestCase(DictionaryOperationsTest))
    
    # Run tests with custom runner
    logger = TestLogger("test_examples.log")
    runner = TestRunner(logger)
    
    # Run the test suite
    print("Running automated tests...")
    print("=" * 70)
    results = runner.run_test_suite(suite)
    
    # Generate report
    report = runner.generate_report("test_examples_report.json")
    
    print("\n" + "=" * 70)
    print("Test Execution Summary:")
    print("=" * 70)
    print(f"Total Tests: {report['total_tests']}")
    print(f"Passed: {report['passed']}")
    print(f"Failed: {report['failed']}")
    print(f"Errors: {report['errors']}")
    print(f"Skipped: {report['skipped']}")
    print("=" * 70)
    
    return report


# Data-driven test example
def example_data_driven_test():
    """Example of data-driven testing."""
    
    def parameterized_addition_test(a, b, expected):
        """Test addition with parameters."""
        result = a + b
        assert result == expected, f"Expected {expected}, got {result}"
    
    # Test data
    test_data = [
        {"a": 1, "b": 1, "expected": 2},
        {"a": 5, "b": 5, "expected": 10},
        {"a": 10, "b": -5, "expected": 5},
        {"a": 0, "b": 0, "expected": 0},
        {"a": -3, "b": -7, "expected": -10},
    ]
    
    # Create and run data-driven test
    logger = TestLogger("data_driven_test.log")
    runner = TestRunner(logger)
    ddt = DataDrivenTest(parameterized_addition_test, test_data)
    
    print("\nRunning Data-Driven Tests...")
    print("=" * 70)
    results = ddt.run(runner)
    
    report = runner.generate_report("data_driven_report.json")
    
    print("\nData-Driven Test Summary:")
    print("=" * 70)
    print(f"Total Tests: {report['total_tests']}")
    print(f"Passed: {report['passed']}")
    print(f"Failed: {report['failed']}")
    print("=" * 70)


if __name__ == "__main__":
    # Run all unit tests
    run_all_tests()
    
    # Run data-driven tests
    print("\n")
    example_data_driven_test()

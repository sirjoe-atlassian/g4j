"""
Test Automation Framework
Generated for Jira Issue: DEV-4

This module provides a simple test automation framework with basic test runner functionality.
"""

import unittest
import sys
from typing import List, Callable, Any
from datetime import datetime


class TestResult:
    """Represents the result of a test execution."""
    
    def __init__(self, test_name: str, passed: bool, error_message: str = None):
        self.test_name = test_name
        self.passed = passed
        self.error_message = error_message
        self.timestamp = datetime.now()
    
    def __repr__(self):
        status = "PASSED" if self.passed else "FAILED"
        return f"TestResult({self.test_name}: {status})"


class TestRunner:
    """A simple test runner for executing automated tests."""
    
    def __init__(self):
        self.results: List[TestResult] = []
    
    def run_test(self, test_func: Callable, test_name: str = None) -> TestResult:
        """
        Run a single test function and capture the result.
        
        Args:
            test_func: The test function to execute
            test_name: Optional name for the test (defaults to function name)
        
        Returns:
            TestResult object containing the test outcome
        """
        if test_name is None:
            test_name = test_func.__name__
        
        try:
            test_func()
            result = TestResult(test_name, passed=True)
        except AssertionError as e:
            result = TestResult(test_name, passed=False, error_message=str(e))
        except Exception as e:
            result = TestResult(test_name, passed=False, error_message=f"Unexpected error: {str(e)}")
        
        self.results.append(result)
        return result
    
    def run_test_suite(self, test_suite: unittest.TestSuite) -> None:
        """
        Run a unittest TestSuite and capture results.
        
        Args:
            test_suite: The unittest TestSuite to execute
        """
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(test_suite)
    
    def print_summary(self) -> None:
        """Print a summary of all test results."""
        total = len(self.results)
        passed = sum(1 for r in self.results if r.passed)
        failed = total - passed
        
        print("\n" + "=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        print(f"Total Tests: {total}")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        print(f"Success Rate: {(passed/total*100) if total > 0 else 0:.2f}%")
        print("=" * 60)
        
        if failed > 0:
            print("\nFailed Tests:")
            for result in self.results:
                if not result.passed:
                    print(f"  - {result.test_name}")
                    if result.error_message:
                        print(f"    Error: {result.error_message}")
        print()
    
    def get_failed_tests(self) -> List[TestResult]:
        """Return a list of all failed test results."""
        return [r for r in self.results if not r.passed]


class BaseTestCase(unittest.TestCase):
    """Base test case class with additional helper methods."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.start_time = datetime.now()
    
    def tearDown(self):
        """Clean up after each test method."""
        self.end_time = datetime.now()
        duration = (self.end_time - self.start_time).total_seconds()
        print(f"Test duration: {duration:.3f}s")
    
    def assert_between(self, value: Any, min_val: Any, max_val: Any, msg: str = None):
        """Assert that a value is between min and max (inclusive)."""
        if not (min_val <= value <= max_val):
            standard_msg = f"{value} is not between {min_val} and {max_val}"
            self.fail(self._formatMessage(msg, standard_msg))
    
    def assert_type(self, obj: Any, expected_type: type, msg: str = None):
        """Assert that an object is of the expected type."""
        if not isinstance(obj, expected_type):
            standard_msg = f"{obj} is not of type {expected_type.__name__}"
            self.fail(self._formatMessage(msg, standard_msg))


# Example test cases
class ExampleTests(BaseTestCase):
    """Example test cases demonstrating the framework."""
    
    def test_addition(self):
        """Test basic addition."""
        result = 2 + 2
        self.assertEqual(result, 4)
    
    def test_string_manipulation(self):
        """Test string operations."""
        text = "hello world"
        self.assertEqual(text.upper(), "HELLO WORLD")
        self.assertTrue(text.startswith("hello"))
    
    def test_list_operations(self):
        """Test list operations."""
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(len(my_list), 5)
        self.assertIn(3, my_list)
        self.assert_type(my_list, list)
    
    def test_custom_assertions(self):
        """Test custom assertion methods."""
        self.assert_between(5, 1, 10)
        self.assert_type("hello", str)


def main():
    """Main entry point for running tests."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(ExampleTests)
    
    # Run tests
    print("Running Test Automation Suite")
    print("=" * 60)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print("EXECUTION COMPLETE")
    print("=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success: {result.wasSuccessful()}")
    print("=" * 60)
    
    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)


if __name__ == "__main__":
    main()

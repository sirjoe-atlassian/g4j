"""
Test Automation Framework
Generated for DEV-4: Test automation generate code

This module provides a basic test automation framework with common testing utilities.
"""

import unittest
from typing import List, Dict, Any, Callable
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class TestResult:
    """Represents the result of a test execution."""
    
    def __init__(self, test_name: str, passed: bool, duration: float, message: str = ""):
        self.test_name = test_name
        self.passed = passed
        self.duration = duration
        self.message = message
    
    def __str__(self):
        status = "PASSED" if self.passed else "FAILED"
        return f"Test: {self.test_name} - {status} ({self.duration:.3f}s) {self.message}"


class TestRunner:
    """Main test runner for executing automated tests."""
    
    def __init__(self):
        self.results: List[TestResult] = []
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
    
    def run_test(self, test_name: str, test_func: Callable) -> TestResult:
        """
        Run a single test function and record the result.
        
        Args:
            test_name: Name of the test
            test_func: Test function to execute
            
        Returns:
            TestResult object containing test execution details
        """
        logger.info(f"Running test: {test_name}")
        start_time = time.time()
        
        try:
            test_func()
            duration = time.time() - start_time
            result = TestResult(test_name, True, duration, "Test passed successfully")
            self.passed_tests += 1
            logger.info(f"✓ {test_name} passed")
        except AssertionError as e:
            duration = time.time() - start_time
            result = TestResult(test_name, False, duration, f"Assertion failed: {str(e)}")
            self.failed_tests += 1
            logger.error(f"✗ {test_name} failed: {str(e)}")
        except Exception as e:
            duration = time.time() - start_time
            result = TestResult(test_name, False, duration, f"Exception: {str(e)}")
            self.failed_tests += 1
            logger.error(f"✗ {test_name} error: {str(e)}")
        
        self.total_tests += 1
        self.results.append(result)
        return result
    
    def run_test_suite(self, test_suite: Dict[str, Callable]) -> List[TestResult]:
        """
        Run a suite of tests.
        
        Args:
            test_suite: Dictionary mapping test names to test functions
            
        Returns:
            List of TestResult objects
        """
        logger.info(f"Starting test suite with {len(test_suite)} tests")
        
        for test_name, test_func in test_suite.items():
            self.run_test(test_name, test_func)
        
        return self.results
    
    def print_summary(self):
        """Print a summary of test execution results."""
        print("\n" + "=" * 70)
        print("TEST EXECUTION SUMMARY")
        print("=" * 70)
        print(f"Total Tests: {self.total_tests}")
        print(f"Passed: {self.passed_tests}")
        print(f"Failed: {self.failed_tests}")
        print(f"Pass Rate: {(self.passed_tests/self.total_tests*100):.2f}%" if self.total_tests > 0 else "N/A")
        print("=" * 70)
        
        if self.results:
            print("\nDetailed Results:")
            for result in self.results:
                print(f"  {result}")
        print()


class TestAssertion:
    """Custom assertion methods for test validation."""
    
    @staticmethod
    def assert_equals(actual: Any, expected: Any, message: str = ""):
        """Assert that two values are equal."""
        if actual != expected:
            error_msg = f"Expected {expected}, but got {actual}"
            if message:
                error_msg = f"{message}: {error_msg}"
            raise AssertionError(error_msg)
    
    @staticmethod
    def assert_true(condition: bool, message: str = ""):
        """Assert that a condition is True."""
        if not condition:
            error_msg = "Expected condition to be True, but it was False"
            if message:
                error_msg = f"{message}: {error_msg}"
            raise AssertionError(error_msg)
    
    @staticmethod
    def assert_false(condition: bool, message: str = ""):
        """Assert that a condition is False."""
        if condition:
            error_msg = "Expected condition to be False, but it was True"
            if message:
                error_msg = f"{message}: {error_msg}"
            raise AssertionError(error_msg)
    
    @staticmethod
    def assert_not_none(value: Any, message: str = ""):
        """Assert that a value is not None."""
        if value is None:
            error_msg = "Expected value to be not None"
            if message:
                error_msg = f"{message}: {error_msg}"
            raise AssertionError(error_msg)
    
    @staticmethod
    def assert_in(item: Any, container: Any, message: str = ""):
        """Assert that an item is in a container."""
        if item not in container:
            error_msg = f"Expected {item} to be in {container}"
            if message:
                error_msg = f"{message}: {error_msg}"
            raise AssertionError(error_msg)


# Example usage
def example_test_suite():
    """Example test suite demonstrating the framework usage."""
    
    def test_addition():
        """Test basic addition."""
        result = 2 + 2
        TestAssertion.assert_equals(result, 4, "Addition test")
    
    def test_string_operations():
        """Test string operations."""
        text = "Hello, World!"
        TestAssertion.assert_in("World", text, "String contains check")
        TestAssertion.assert_equals(len(text), 13, "String length check")
    
    def test_boolean_logic():
        """Test boolean operations."""
        TestAssertion.assert_true(True, "Boolean true check")
        TestAssertion.assert_false(False, "Boolean false check")
    
    def test_list_operations():
        """Test list operations."""
        my_list = [1, 2, 3, 4, 5]
        TestAssertion.assert_equals(len(my_list), 5, "List length check")
        TestAssertion.assert_in(3, my_list, "List contains check")
    
    # Create test suite dictionary
    test_suite = {
        "test_addition": test_addition,
        "test_string_operations": test_string_operations,
        "test_boolean_logic": test_boolean_logic,
        "test_list_operations": test_list_operations,
    }
    
    # Run tests
    runner = TestRunner()
    runner.run_test_suite(test_suite)
    runner.print_summary()


if __name__ == "__main__":
    print("Test Automation Framework - DEV-4")
    print("Running example test suite...\n")
    example_test_suite()

"""
Test Automation Framework
This module provides a basic test automation framework with common testing utilities.
"""

import unittest
import time
from typing import Any, Callable, Optional
from functools import wraps


class TestBase(unittest.TestCase):
    """Base test class with common setup and teardown methods."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.start_time = time.time()
        print(f"\nStarting test: {self._testMethodName}")
    
    def tearDown(self):
        """Clean up after each test method."""
        elapsed = time.time() - self.start_time
        print(f"Test {self._testMethodName} completed in {elapsed:.3f}s")
    
    def assert_equals_with_message(self, expected: Any, actual: Any, message: str = ""):
        """Assert equality with custom message."""
        self.assertEqual(expected, actual, f"{message}\nExpected: {expected}, Actual: {actual}")
    
    def assert_in_range(self, value: float, min_val: float, max_val: float, message: str = ""):
        """Assert that a value is within a specified range."""
        self.assertTrue(
            min_val <= value <= max_val,
            f"{message}\nValue {value} is not in range [{min_val}, {max_val}]"
        )


def retry_on_failure(max_attempts: int = 3, delay: float = 1.0):
    """
    Decorator to retry a test function on failure.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Delay in seconds between retries
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        print(f"Attempt {attempt + 1} failed, retrying in {delay}s...")
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator


def timeout(seconds: int):
    """
    Decorator to add timeout to test functions.
    
    Args:
        seconds: Timeout in seconds
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            import signal
            
            def timeout_handler(signum, frame):
                raise TimeoutError(f"Test {func.__name__} timed out after {seconds} seconds")
            
            # Set the signal handler and alarm
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(seconds)
            
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)  # Disable the alarm
            
            return result
        return wrapper
    return decorator


class TestRunner:
    """Custom test runner with additional reporting capabilities."""
    
    def __init__(self, verbosity: int = 2):
        """
        Initialize the test runner.
        
        Args:
            verbosity: Level of detail in test output (0=quiet, 1=normal, 2=verbose)
        """
        self.verbosity = verbosity
        self.results = []
    
    def run_tests(self, test_suite: unittest.TestSuite) -> unittest.TestResult:
        """
        Run a test suite and return the results.
        
        Args:
            test_suite: The test suite to run
            
        Returns:
            Test results object
        """
        runner = unittest.TextTestRunner(verbosity=self.verbosity)
        result = runner.run(test_suite)
        self.results.append(result)
        return result
    
    def generate_summary(self) -> dict:
        """
        Generate a summary of all test results.
        
        Returns:
            Dictionary containing test statistics
        """
        total_tests = sum(r.testsRun for r in self.results)
        total_failures = sum(len(r.failures) for r in self.results)
        total_errors = sum(len(r.errors) for r in self.results)
        total_skipped = sum(len(r.skipped) for r in self.results)
        
        return {
            'total_tests': total_tests,
            'passed': total_tests - total_failures - total_errors - total_skipped,
            'failures': total_failures,
            'errors': total_errors,
            'skipped': total_skipped,
            'success_rate': ((total_tests - total_failures - total_errors) / total_tests * 100) if total_tests > 0 else 0
        }


class DataDrivenTest:
    """Helper class for data-driven testing."""
    
    @staticmethod
    def run_with_data(test_func: Callable, test_data: list) -> list:
        """
        Run a test function with multiple data sets.
        
        Args:
            test_func: The test function to run
            test_data: List of data sets to pass to the test function
            
        Returns:
            List of results from each test run
        """
        results = []
        for i, data in enumerate(test_data):
            print(f"\nRunning test with data set {i + 1}/{len(test_data)}")
            try:
                result = test_func(data)
                results.append({'status': 'passed', 'data': data, 'result': result})
            except Exception as e:
                results.append({'status': 'failed', 'data': data, 'error': str(e)})
        return results


# Example test cases
class ExampleTests(TestBase):
    """Example test cases demonstrating the framework."""
    
    def test_basic_assertion(self):
        """Test basic assertion functionality."""
        self.assertEqual(1 + 1, 2)
        self.assertTrue(True)
        self.assertIsNotNone("value")
    
    def test_custom_assertion(self):
        """Test custom assertion methods."""
        self.assert_equals_with_message(10, 10, "Values should be equal")
        self.assert_in_range(5.5, 5.0, 6.0, "Value should be in range")
    
    @retry_on_failure(max_attempts=2, delay=0.5)
    def test_with_retry(self):
        """Test with retry decorator."""
        self.assertTrue(True)


if __name__ == '__main__':
    # Run example tests
    suite = unittest.TestLoader().loadTestsFromTestCase(ExampleTests)
    runner = TestRunner(verbosity=2)
    result = runner.run_tests(suite)
    
    # Print summary
    summary = runner.generate_summary()
    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)
    print(f"Total Tests: {summary['total_tests']}")
    print(f"Passed: {summary['passed']}")
    print(f"Failures: {summary['failures']}")
    print(f"Errors: {summary['errors']}")
    print(f"Skipped: {summary['skipped']}")
    print(f"Success Rate: {summary['success_rate']:.2f}%")

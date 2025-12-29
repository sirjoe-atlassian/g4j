"""
Test Automation Framework
This module provides a basic test automation framework with common testing utilities.
"""

import unittest
import time
from typing import Callable, Any, Optional
from functools import wraps


class TestLogger:
    """Simple logger for test execution."""
    
    @staticmethod
    def log(message: str, level: str = "INFO") -> None:
        """Log a message with timestamp and level."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{level}] {message}")


def retry(max_attempts: int = 3, delay: float = 1.0):
    """
    Decorator to retry a test function on failure.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Delay in seconds between retries
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    TestLogger.log(f"Attempt {attempt}/{max_attempts} for {func.__name__}")
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    TestLogger.log(
                        f"Attempt {attempt} failed: {str(e)}", 
                        level="WARNING"
                    )
                    if attempt < max_attempts:
                        time.sleep(delay)
            TestLogger.log(
                f"All {max_attempts} attempts failed for {func.__name__}", 
                level="ERROR"
            )
            raise last_exception
        return wrapper
    return decorator


class BaseTestCase(unittest.TestCase):
    """Base test case with common setup and utilities."""
    
    def setUp(self) -> None:
        """Set up test fixtures."""
        TestLogger.log(f"Starting test: {self._testMethodName}")
        self.start_time = time.time()
    
    def tearDown(self) -> None:
        """Clean up after test."""
        duration = time.time() - self.start_time
        TestLogger.log(
            f"Completed test: {self._testMethodName} in {duration:.2f}s"
        )
    
    def assert_eventually(
        self, 
        condition: Callable[[], bool], 
        timeout: float = 10.0, 
        interval: float = 0.5,
        message: Optional[str] = None
    ) -> None:
        """
        Assert that a condition becomes true within a timeout period.
        
        Args:
            condition: Callable that returns boolean
            timeout: Maximum time to wait in seconds
            interval: Time between checks in seconds
            message: Optional failure message
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            if condition():
                return
            time.sleep(interval)
        
        fail_msg = message or f"Condition not met within {timeout}s"
        self.fail(fail_msg)


class SampleTestSuite(BaseTestCase):
    """Sample test suite demonstrating the framework."""
    
    def test_basic_assertion(self) -> None:
        """Test basic assertion functionality."""
        self.assertEqual(1 + 1, 2)
        self.assertTrue(True)
        self.assertFalse(False)
    
    def test_string_operations(self) -> None:
        """Test string operations."""
        test_string = "Hello, World!"
        self.assertIn("World", test_string)
        self.assertEqual(test_string.lower(), "hello, world!")
    
    @retry(max_attempts=2, delay=0.5)
    def test_with_retry(self) -> None:
        """Test with retry decorator."""
        self.assertTrue(True)
    
    def test_eventually_assertion(self) -> None:
        """Test eventually assertion."""
        counter = {"value": 0}
        
        def increment_until_five() -> bool:
            counter["value"] += 1
            return counter["value"] >= 5
        
        self.assert_eventually(
            increment_until_five,
            timeout=5.0,
            message="Counter did not reach 5"
        )


def run_tests() -> None:
    """Run all tests in the suite."""
    TestLogger.log("Starting test automation suite")
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(SampleTestSuite)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Log results
    TestLogger.log(f"Tests run: {result.testsRun}")
    TestLogger.log(f"Failures: {len(result.failures)}")
    TestLogger.log(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        TestLogger.log("All tests passed!", level="SUCCESS")
    else:
        TestLogger.log("Some tests failed!", level="ERROR")


if __name__ == "__main__":
    run_tests()

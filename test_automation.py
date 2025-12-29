"""
Test Automation Framework
This module provides a basic test automation framework for automated testing.
"""

import unittest
from typing import List, Callable, Any
import time


class TestResult:
    """Represents the result of a test execution."""
    
    def __init__(self, test_name: str, passed: bool, duration: float, error_message: str = None):
        self.test_name = test_name
        self.passed = passed
        self.duration = duration
        self.error_message = error_message
    
    def __repr__(self):
        status = "PASSED" if self.passed else "FAILED"
        result = f"Test: {self.test_name} - {status} (Duration: {self.duration:.3f}s)"
        if self.error_message:
            result += f"\n  Error: {self.error_message}"
        return result


class TestAutomation:
    """
    A simple test automation framework that allows you to register and run tests.
    """
    
    def __init__(self):
        self.tests: List[tuple[str, Callable]] = []
        self.results: List[TestResult] = []
        self.setup_func: Callable = None
        self.teardown_func: Callable = None
    
    def register_test(self, name: str, test_func: Callable):
        """
        Register a test function to be executed.
        
        Args:
            name: The name of the test
            test_func: The function to execute for this test
        """
        self.tests.append((name, test_func))
    
    def set_setup(self, setup_func: Callable):
        """
        Set a setup function to run before each test.
        
        Args:
            setup_func: The setup function to execute before each test
        """
        self.setup_func = setup_func
    
    def set_teardown(self, teardown_func: Callable):
        """
        Set a teardown function to run after each test.
        
        Args:
            teardown_func: The teardown function to execute after each test
        """
        self.teardown_func = teardown_func
    
    def run_test(self, name: str, test_func: Callable) -> TestResult:
        """
        Run a single test and return the result.
        
        Args:
            name: The name of the test
            test_func: The test function to execute
            
        Returns:
            TestResult object containing the test execution details
        """
        start_time = time.time()
        error_message = None
        passed = False
        
        try:
            if self.setup_func:
                self.setup_func()
            
            test_func()
            passed = True
            
        except AssertionError as e:
            error_message = f"Assertion failed: {str(e)}"
        except Exception as e:
            error_message = f"Exception: {type(e).__name__}: {str(e)}"
        finally:
            if self.teardown_func:
                try:
                    self.teardown_func()
                except Exception as e:
                    if not error_message:
                        error_message = f"Teardown failed: {str(e)}"
                        passed = False
        
        duration = time.time() - start_time
        return TestResult(name, passed, duration, error_message)
    
    def run_all_tests(self) -> List[TestResult]:
        """
        Run all registered tests and return the results.
        
        Returns:
            List of TestResult objects
        """
        self.results = []
        
        print(f"\n{'='*60}")
        print(f"Running {len(self.tests)} test(s)...")
        print(f"{'='*60}\n")
        
        for name, test_func in self.tests:
            result = self.run_test(name, test_func)
            self.results.append(result)
            print(result)
        
        self._print_summary()
        return self.results
    
    def _print_summary(self):
        """Print a summary of all test results."""
        passed = sum(1 for r in self.results if r.passed)
        failed = sum(1 for r in self.results if not r.passed)
        total_duration = sum(r.duration for r in self.results)
        
        print(f"\n{'='*60}")
        print(f"Test Summary:")
        print(f"  Total: {len(self.results)}")
        print(f"  Passed: {passed}")
        print(f"  Failed: {failed}")
        print(f"  Total Duration: {total_duration:.3f}s")
        print(f"{'='*60}\n")
    
    def get_results(self) -> List[TestResult]:
        """
        Get the results of all executed tests.
        
        Returns:
            List of TestResult objects
        """
        return self.results


# Example usage
if __name__ == "__main__":
    # Create test automation instance
    automation = TestAutomation()
    
    # Define setup and teardown
    def setup():
        print("  [Setup] Preparing test environment...")
    
    def teardown():
        print("  [Teardown] Cleaning up...")
    
    automation.set_setup(setup)
    automation.set_teardown(teardown)
    
    # Register some example tests
    def test_example_pass():
        """Example test that passes."""
        assert 1 + 1 == 2
        assert "hello".upper() == "HELLO"
    
    def test_example_fail():
        """Example test that fails."""
        assert 1 + 1 == 3, "Math is broken!"
    
    def test_string_operations():
        """Test string operations."""
        test_string = "Test Automation"
        assert len(test_string) == 15
        assert test_string.lower() == "test automation"
        assert test_string.startswith("Test")
    
    def test_list_operations():
        """Test list operations."""
        test_list = [1, 2, 3, 4, 5]
        assert len(test_list) == 5
        assert sum(test_list) == 15
        assert max(test_list) == 5
    
    # Register tests
    automation.register_test("test_example_pass", test_example_pass)
    automation.register_test("test_example_fail", test_example_fail)
    automation.register_test("test_string_operations", test_string_operations)
    automation.register_test("test_list_operations", test_list_operations)
    
    # Run all tests
    results = automation.run_all_tests()
    
    # Exit with appropriate code
    failed_count = sum(1 for r in results if not r.passed)
    exit(0 if failed_count == 0 else 1)

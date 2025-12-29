"""
Test Automation Framework
Generated for DEV-4: Test automation generate code

This module provides a flexible test automation framework with support for:
- Unit testing
- Integration testing
- End-to-end testing
- Test reporting and logging
"""

import unittest
import logging
from typing import Callable, Any, Dict, List
from datetime import datetime
import json


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class TestResult:
    """Represents the result of a test execution."""
    
    def __init__(self, test_name: str, status: str, duration: float, 
                 message: str = "", error: Exception = None):
        self.test_name = test_name
        self.status = status  # 'PASSED', 'FAILED', 'SKIPPED', 'ERROR'
        self.duration = duration
        self.message = message
        self.error = error
        self.timestamp = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert test result to dictionary format."""
        return {
            'test_name': self.test_name,
            'status': self.status,
            'duration': self.duration,
            'message': self.message,
            'error': str(self.error) if self.error else None,
            'timestamp': self.timestamp
        }


class TestRunner:
    """Main test runner for executing automated tests."""
    
    def __init__(self):
        self.results: List[TestResult] = []
        self.setup_hooks: List[Callable] = []
        self.teardown_hooks: List[Callable] = []
    
    def add_setup_hook(self, hook: Callable) -> None:
        """Add a setup hook to run before tests."""
        self.setup_hooks.append(hook)
    
    def add_teardown_hook(self, hook: Callable) -> None:
        """Add a teardown hook to run after tests."""
        self.teardown_hooks.append(hook)
    
    def run_setup(self) -> None:
        """Execute all setup hooks."""
        logger.info("Running setup hooks...")
        for hook in self.setup_hooks:
            try:
                hook()
            except Exception as e:
                logger.error(f"Setup hook failed: {e}")
                raise
    
    def run_teardown(self) -> None:
        """Execute all teardown hooks."""
        logger.info("Running teardown hooks...")
        for hook in self.teardown_hooks:
            try:
                hook()
            except Exception as e:
                logger.error(f"Teardown hook failed: {e}")
    
    def run_test(self, test_func: Callable, test_name: str = None) -> TestResult:
        """Run a single test function and capture the result."""
        if test_name is None:
            test_name = test_func.__name__
        
        logger.info(f"Running test: {test_name}")
        start_time = datetime.now()
        
        try:
            test_func()
            duration = (datetime.now() - start_time).total_seconds()
            result = TestResult(test_name, 'PASSED', duration, "Test passed successfully")
            logger.info(f"✓ {test_name} PASSED ({duration:.3f}s)")
        except AssertionError as e:
            duration = (datetime.now() - start_time).total_seconds()
            result = TestResult(test_name, 'FAILED', duration, str(e), e)
            logger.error(f"✗ {test_name} FAILED ({duration:.3f}s): {e}")
        except Exception as e:
            duration = (datetime.now() - start_time).total_seconds()
            result = TestResult(test_name, 'ERROR', duration, str(e), e)
            logger.error(f"✗ {test_name} ERROR ({duration:.3f}s): {e}")
        
        self.results.append(result)
        return result
    
    def run_test_suite(self, test_suite: unittest.TestSuite) -> None:
        """Run a unittest TestSuite."""
        logger.info("Running unittest test suite...")
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(test_suite)
        
        # Convert unittest results to our format
        for test, traceback in result.failures:
            self.results.append(TestResult(
                str(test), 'FAILED', 0, traceback
            ))
        
        for test, traceback in result.errors:
            self.results.append(TestResult(
                str(test), 'ERROR', 0, traceback
            ))
    
    def generate_report(self) -> Dict[str, Any]:
        """Generate a comprehensive test report."""
        total_tests = len(self.results)
        passed = sum(1 for r in self.results if r.status == 'PASSED')
        failed = sum(1 for r in self.results if r.status == 'FAILED')
        errors = sum(1 for r in self.results if r.status == 'ERROR')
        skipped = sum(1 for r in self.results if r.status == 'SKIPPED')
        
        total_duration = sum(r.duration for r in self.results)
        
        report = {
            'summary': {
                'total_tests': total_tests,
                'passed': passed,
                'failed': failed,
                'errors': errors,
                'skipped': skipped,
                'success_rate': (passed / total_tests * 100) if total_tests > 0 else 0,
                'total_duration': total_duration
            },
            'results': [r.to_dict() for r in self.results],
            'timestamp': datetime.now().isoformat()
        }
        
        return report
    
    def save_report(self, filename: str = 'test_report.json') -> None:
        """Save test report to a JSON file."""
        report = self.generate_report()
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        logger.info(f"Test report saved to {filename}")
    
    def print_summary(self) -> None:
        """Print a summary of test results."""
        report = self.generate_report()
        summary = report['summary']
        
        print("\n" + "="*60)
        print("TEST EXECUTION SUMMARY")
        print("="*60)
        print(f"Total Tests:     {summary['total_tests']}")
        print(f"Passed:          {summary['passed']} ✓")
        print(f"Failed:          {summary['failed']} ✗")
        print(f"Errors:          {summary['errors']} ✗")
        print(f"Skipped:         {summary['skipped']} -")
        print(f"Success Rate:    {summary['success_rate']:.2f}%")
        print(f"Total Duration:  {summary['total_duration']:.3f}s")
        print("="*60 + "\n")


class TestCase(unittest.TestCase):
    """Base test case class with additional utilities."""
    
    def assert_in_range(self, value: float, min_val: float, max_val: float, 
                       msg: str = None) -> None:
        """Assert that a value is within a specified range."""
        if not (min_val <= value <= max_val):
            raise AssertionError(
                msg or f"{value} is not in range [{min_val}, {max_val}]"
            )
    
    def assert_json_equal(self, actual: Dict, expected: Dict, msg: str = None) -> None:
        """Assert that two JSON objects are equal."""
        if actual != expected:
            raise AssertionError(
                msg or f"JSON objects do not match:\nActual: {actual}\nExpected: {expected}"
            )


# Example usage and sample tests
class SampleTests(TestCase):
    """Sample test cases demonstrating the framework."""
    
    def test_addition(self):
        """Test basic addition."""
        result = 2 + 2
        self.assertEqual(result, 4)
    
    def test_string_operations(self):
        """Test string operations."""
        text = "hello world"
        self.assertTrue(text.startswith("hello"))
        self.assertIn("world", text)
    
    def test_list_operations(self):
        """Test list operations."""
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(len(numbers), 5)
        self.assertIn(3, numbers)
    
    def test_range_assertion(self):
        """Test custom range assertion."""
        value = 50
        self.assert_in_range(value, 0, 100)


def main():
    """Main entry point for test execution."""
    runner = TestRunner()
    
    # Add setup and teardown hooks
    runner.add_setup_hook(lambda: logger.info("Test suite starting..."))
    runner.add_teardown_hook(lambda: logger.info("Test suite completed."))
    
    # Run setup
    runner.run_setup()
    
    # Create and run test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(SampleTests)
    runner.run_test_suite(suite)
    
    # Run teardown
    runner.run_teardown()
    
    # Print summary and save report
    runner.print_summary()
    runner.save_report()


if __name__ == '__main__':
    main()

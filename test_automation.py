"""
Test Automation Framework
A flexible and extensible test automation framework for Python applications.
"""

import unittest
import logging
from typing import List, Dict, Any, Callable
from datetime import datetime
import json


class TestLogger:
    """Logger for test execution and results."""
    
    def __init__(self, log_file: str = "test_results.log"):
        self.log_file = log_file
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def log_test_start(self, test_name: str):
        """Log the start of a test."""
        self.logger.info(f"Starting test: {test_name}")
    
    def log_test_end(self, test_name: str, status: str):
        """Log the end of a test with status."""
        self.logger.info(f"Test {test_name} completed with status: {status}")
    
    def log_error(self, test_name: str, error: str):
        """Log test errors."""
        self.logger.error(f"Error in test {test_name}: {error}")


class TestResult:
    """Represents the result of a test execution."""
    
    def __init__(self, test_name: str, status: str, duration: float, 
                 error_message: str = None):
        self.test_name = test_name
        self.status = status  # 'passed', 'failed', 'skipped', 'error'
        self.duration = duration
        self.error_message = error_message
        self.timestamp = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert test result to dictionary."""
        return {
            'test_name': self.test_name,
            'status': self.status,
            'duration': self.duration,
            'error_message': self.error_message,
            'timestamp': self.timestamp
        }


class TestRunner:
    """Test runner for executing automated tests."""
    
    def __init__(self, logger: TestLogger = None):
        self.logger = logger or TestLogger()
        self.results: List[TestResult] = []
    
    def run_test(self, test_func: Callable, test_name: str = None) -> TestResult:
        """Run a single test function and return the result."""
        if test_name is None:
            test_name = test_func.__name__
        
        self.logger.log_test_start(test_name)
        start_time = datetime.now()
        
        try:
            test_func()
            status = 'passed'
            error_message = None
        except AssertionError as e:
            status = 'failed'
            error_message = str(e)
            self.logger.log_error(test_name, error_message)
        except Exception as e:
            status = 'error'
            error_message = str(e)
            self.logger.log_error(test_name, error_message)
        
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        result = TestResult(test_name, status, duration, error_message)
        self.results.append(result)
        self.logger.log_test_end(test_name, status)
        
        return result
    
    def run_test_suite(self, test_suite: unittest.TestSuite) -> List[TestResult]:
        """Run a unittest TestSuite."""
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(test_suite)
        
        # Convert unittest results to our TestResult format
        for test, traceback in result.failures:
            test_name = str(test)
            self.results.append(TestResult(test_name, 'failed', 0, traceback))
        
        for test, traceback in result.errors:
            test_name = str(test)
            self.results.append(TestResult(test_name, 'error', 0, traceback))
        
        return self.results
    
    def generate_report(self, output_file: str = "test_report.json"):
        """Generate a JSON report of test results."""
        report = {
            'total_tests': len(self.results),
            'passed': sum(1 for r in self.results if r.status == 'passed'),
            'failed': sum(1 for r in self.results if r.status == 'failed'),
            'errors': sum(1 for r in self.results if r.status == 'error'),
            'skipped': sum(1 for r in self.results if r.status == 'skipped'),
            'results': [r.to_dict() for r in self.results]
        }
        
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        self.logger.logger.info(f"Test report generated: {output_file}")
        return report


class TestCase(unittest.TestCase):
    """Extended TestCase with additional assertion methods."""
    
    def assertBetween(self, value, min_value, max_value, msg=None):
        """Assert that a value is between min and max (inclusive)."""
        if not (min_value <= value <= max_value):
            standardMsg = f"{value} not between {min_value} and {max_value}"
            self.fail(self._formatMessage(msg, standardMsg))
    
    def assertResponse(self, response, expected_status: int, msg=None):
        """Assert HTTP response status code."""
        if hasattr(response, 'status_code'):
            self.assertEqual(response.status_code, expected_status, msg)
        else:
            self.fail("Response object does not have status_code attribute")
    
    def assertContainsKey(self, dictionary: Dict, key: str, msg=None):
        """Assert that a dictionary contains a specific key."""
        if key not in dictionary:
            standardMsg = f"Key '{key}' not found in dictionary"
            self.fail(self._formatMessage(msg, standardMsg))


class DataDrivenTest:
    """Base class for data-driven testing."""
    
    def __init__(self, test_func: Callable, test_data: List[Dict[str, Any]]):
        self.test_func = test_func
        self.test_data = test_data
    
    def run(self, runner: TestRunner) -> List[TestResult]:
        """Run the test function with each data set."""
        results = []
        for i, data in enumerate(self.test_data):
            test_name = f"{self.test_func.__name__}_data_{i}"
            result = runner.run_test(
                lambda: self.test_func(**data),
                test_name
            )
            results.append(result)
        return results


# Example usage
if __name__ == "__main__":
    # Create logger and runner
    logger = TestLogger("automation_tests.log")
    runner = TestRunner(logger)
    
    # Example test function
    def test_addition():
        assert 2 + 2 == 4, "Addition test failed"
    
    def test_subtraction():
        assert 5 - 3 == 2, "Subtraction test failed"
    
    def test_multiplication():
        assert 3 * 4 == 12, "Multiplication test failed"
    
    def test_division():
        assert 10 / 2 == 5, "Division test failed"
    
    # Run individual tests
    runner.run_test(test_addition)
    runner.run_test(test_subtraction)
    runner.run_test(test_multiplication)
    runner.run_test(test_division)
    
    # Generate report
    report = runner.generate_report("example_test_report.json")
    print(f"\nTest Summary:")
    print(f"Total Tests: {report['total_tests']}")
    print(f"Passed: {report['passed']}")
    print(f"Failed: {report['failed']}")
    print(f"Errors: {report['errors']}")

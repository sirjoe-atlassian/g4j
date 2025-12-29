#!/usr/bin/env python3
"""
Test Automation Framework
A flexible and extensible test automation framework with support for multiple test types.
"""

import unittest
import sys
from datetime import datetime
from typing import List, Dict, Any, Optional
import json


class TestResult:
    """Stores test execution results."""
    
    def __init__(self, test_name: str, status: str, duration: float, 
                 error_message: Optional[str] = None):
        self.test_name = test_name
        self.status = status
        self.duration = duration
        self.error_message = error_message
        self.timestamp = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert result to dictionary format."""
        return {
            'test_name': self.test_name,
            'status': self.status,
            'duration': self.duration,
            'error_message': self.error_message,
            'timestamp': self.timestamp
        }


class TestAutomationFramework:
    """Main test automation framework class."""
    
    def __init__(self, test_suite_name: str = "Default Test Suite"):
        self.test_suite_name = test_suite_name
        self.results: List[TestResult] = []
        self.start_time = None
        self.end_time = None
    
    def run_test_suite(self, test_loader: unittest.TestLoader, 
                      test_pattern: str = "test*.py") -> bool:
        """
        Run a test suite and collect results.
        
        Args:
            test_loader: unittest.TestLoader instance
            test_pattern: Pattern to match test files
            
        Returns:
            True if all tests passed, False otherwise
        """
        self.start_time = datetime.now()
        
        # Discover and run tests
        suite = test_loader.discover('.', pattern=test_pattern)
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        self.end_time = datetime.now()
        
        # Store results
        for test, error in result.errors:
            self.results.append(TestResult(
                test_name=str(test),
                status='ERROR',
                duration=0.0,
                error_message=str(error)
            ))
        
        for test, failure in result.failures:
            self.results.append(TestResult(
                test_name=str(test),
                status='FAILED',
                duration=0.0,
                error_message=str(failure)
            ))
        
        # Calculate passed tests
        total_tests = result.testsRun
        failed_tests = len(result.failures) + len(result.errors)
        passed_tests = total_tests - failed_tests
        
        for i in range(passed_tests):
            self.results.append(TestResult(
                test_name=f"test_{i}",
                status='PASSED',
                duration=0.0
            ))
        
        return result.wasSuccessful()
    
    def generate_report(self, output_format: str = "json") -> str:
        """
        Generate test execution report.
        
        Args:
            output_format: Format for the report ('json' or 'text')
            
        Returns:
            Formatted report string
        """
        if output_format == "json":
            return self._generate_json_report()
        else:
            return self._generate_text_report()
    
    def _generate_json_report(self) -> str:
        """Generate JSON format report."""
        report = {
            'test_suite': self.test_suite_name,
            'start_time': self.start_time.isoformat() if self.start_time else None,
            'end_time': self.end_time.isoformat() if self.end_time else None,
            'total_tests': len(self.results),
            'passed': sum(1 for r in self.results if r.status == 'PASSED'),
            'failed': sum(1 for r in self.results if r.status == 'FAILED'),
            'errors': sum(1 for r in self.results if r.status == 'ERROR'),
            'results': [r.to_dict() for r in self.results]
        }
        return json.dumps(report, indent=2)
    
    def _generate_text_report(self) -> str:
        """Generate text format report."""
        lines = [
            f"=" * 80,
            f"Test Suite: {self.test_suite_name}",
            f"=" * 80,
            f"Start Time: {self.start_time}",
            f"End Time: {self.end_time}",
            f"Total Tests: {len(self.results)}",
            f"Passed: {sum(1 for r in self.results if r.status == 'PASSED')}",
            f"Failed: {sum(1 for r in self.results if r.status == 'FAILED')}",
            f"Errors: {sum(1 for r in self.results if r.status == 'ERROR')}",
            f"=" * 80,
            "\nDetailed Results:\n"
        ]
        
        for result in self.results:
            lines.append(f"  {result.test_name}: {result.status}")
            if result.error_message:
                lines.append(f"    Error: {result.error_message}")
        
        return "\n".join(lines)
    
    def save_report(self, filename: str, output_format: str = "json"):
        """Save report to a file."""
        report = self.generate_report(output_format)
        with open(filename, 'w') as f:
            f.write(report)
        print(f"Report saved to {filename}")


class BaseTestCase(unittest.TestCase):
    """Base test case class with common setup and teardown."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_start_time = datetime.now()
        print(f"\nStarting test: {self._testMethodName}")
    
    def tearDown(self):
        """Clean up after test."""
        test_duration = (datetime.now() - self.test_start_time).total_seconds()
        print(f"Completed test: {self._testMethodName} in {test_duration:.2f}s")
    
    def assert_response_code(self, actual: int, expected: int, message: str = ""):
        """Custom assertion for response codes."""
        self.assertEqual(actual, expected, 
                        f"Response code mismatch. {message}")
    
    def assert_contains(self, container: Any, item: Any, message: str = ""):
        """Custom assertion to check if item is in container."""
        self.assertIn(item, container, 
                     f"Item not found in container. {message}")


def run_tests(pattern: str = "test*.py", suite_name: str = "Test Suite"):
    """
    Main function to run tests with the automation framework.
    
    Args:
        pattern: Pattern to match test files
        suite_name: Name of the test suite
    """
    framework = TestAutomationFramework(suite_name)
    loader = unittest.TestLoader()
    
    print(f"Running {suite_name}...")
    print(f"Test pattern: {pattern}")
    
    success = framework.run_test_suite(loader, pattern)
    
    # Generate and save reports
    print("\nGenerating reports...")
    framework.save_report("test_report.json", "json")
    framework.save_report("test_report.txt", "text")
    
    # Print summary
    print("\n" + framework.generate_report("text"))
    
    return 0 if success else 1


if __name__ == "__main__":
    # Allow command-line arguments for test pattern and suite name
    pattern = sys.argv[1] if len(sys.argv) > 1 else "test*.py"
    suite_name = sys.argv[2] if len(sys.argv) > 2 else "Test Suite"
    
    exit_code = run_tests(pattern, suite_name)
    sys.exit(exit_code)

#!/usr/bin/env python3
"""
Test Automation Runner
This module provides a simple test runner for automated testing.
"""

import unittest
import sys
import os
from datetime import datetime


class TestRunner:
    """Main test runner class for executing automated tests."""
    
    def __init__(self, test_directory='tests'):
        """
        Initialize the test runner.
        
        Args:
            test_directory (str): Directory containing test files
        """
        self.test_directory = test_directory
        self.test_suite = unittest.TestSuite()
        
    def discover_tests(self, pattern='test_*.py'):
        """
        Discover all test files in the test directory.
        
        Args:
            pattern (str): Pattern to match test files
            
        Returns:
            unittest.TestSuite: Suite of discovered tests
        """
        loader = unittest.TestLoader()
        self.test_suite = loader.discover(
            start_dir=self.test_directory,
            pattern=pattern,
            top_level_dir=None
        )
        return self.test_suite
    
    def run_tests(self, verbosity=2):
        """
        Run all discovered tests.
        
        Args:
            verbosity (int): Level of detail in output (0-2)
            
        Returns:
            unittest.TestResult: Results of test execution
        """
        runner = unittest.TextTestRunner(verbosity=verbosity)
        result = runner.run(self.test_suite)
        return result
    
    def generate_report(self, result):
        """
        Generate a test report.
        
        Args:
            result (unittest.TestResult): Test execution results
            
        Returns:
            dict: Dictionary containing test statistics
        """
        report = {
            'timestamp': datetime.now().isoformat(),
            'total_tests': result.testsRun,
            'failures': len(result.failures),
            'errors': len(result.errors),
            'skipped': len(result.skipped),
            'success_rate': ((result.testsRun - len(result.failures) - len(result.errors)) 
                           / result.testsRun * 100) if result.testsRun > 0 else 0
        }
        return report


def main():
    """Main entry point for test runner."""
    print("=" * 70)
    print("Test Automation Runner")
    print("=" * 70)
    
    # Initialize test runner
    runner = TestRunner(test_directory='tests')
    
    # Discover tests
    print(f"\nDiscovering tests in 'tests' directory...")
    runner.discover_tests()
    
    # Run tests
    print("\nRunning tests...\n")
    result = runner.run_tests(verbosity=2)
    
    # Generate report
    report = runner.generate_report(result)
    
    print("\n" + "=" * 70)
    print("Test Summary")
    print("=" * 70)
    print(f"Timestamp: {report['timestamp']}")
    print(f"Total Tests: {report['total_tests']}")
    print(f"Failures: {report['failures']}")
    print(f"Errors: {report['errors']}")
    print(f"Skipped: {report['skipped']}")
    print(f"Success Rate: {report['success_rate']:.2f}%")
    print("=" * 70)
    
    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)


if __name__ == '__main__':
    main()

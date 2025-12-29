"""
Test runner module for executing automated tests.
Provides utilities for running tests and generating reports.
"""

import unittest
import sys
from io import StringIO


def run_all_tests(verbosity=2):
    """
    Run all tests in the tests directory.
    
    Args:
        verbosity (int): Level of output detail (0=quiet, 1=normal, 2=verbose)
    
    Returns:
        unittest.TestResult: Results of the test run
    """
    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)
    
    return result


def run_specific_test(test_module, test_class=None, test_method=None):
    """
    Run a specific test or test class.
    
    Args:
        test_module (str): Name of the test module
        test_class (str, optional): Name of the test class
        test_method (str, optional): Name of the test method
    
    Returns:
        unittest.TestResult: Results of the test run
    """
    loader = unittest.TestLoader()
    
    if test_method and test_class:
        suite = loader.loadTestsFromName(f'{test_module}.{test_class}.{test_method}')
    elif test_class:
        suite = loader.loadTestsFromName(f'{test_module}.{test_class}')
    else:
        suite = loader.loadTestsFromModule(__import__(test_module))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result


if __name__ == '__main__':
    print("Running all tests...")
    print("=" * 70)
    result = run_all_tests()
    print("=" * 70)
    print(f"\nTests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped)}")
    
    sys.exit(0 if result.wasSuccessful() else 1)

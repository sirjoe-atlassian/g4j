"""
Unit tests for the test automation framework itself.
Generated for Jira issue DEV-4: Test automation generate code

This file contains tests to verify the test automation framework works correctly.
"""

import unittest
import sys
import os

# Add parent directory to path to import test_automation module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from test_automation import (
    TestCase, TestSuite, TestResult, CustomAssertions
)


class TestTestCase(unittest.TestCase):
    """Unit tests for TestCase class."""
    
    def test_test_case_initialization(self):
        """Test that TestCase initializes correctly."""
        tc = TestCase("test_name", "test_description", ["tag1", "tag2"])
        
        self.assertEqual(tc.name, "test_name")
        self.assertEqual(tc.description, "test_description")
        self.assertEqual(tc.tags, ["tag1", "tag2"])
        self.assertIsNone(tc.result)
        self.assertEqual(tc.duration, 0.0)
    
    def test_test_case_execution_success(self):
        """Test that TestCase executes successfully with passing test."""
        tc = TestCase("test_pass", "Should pass")
        
        def passing_test():
            assert True
        
        result = tc.execute(passing_test)
        
        self.assertEqual(result, TestResult.PASSED)
        self.assertEqual(tc.result, TestResult.PASSED)
        self.assertIsNone(tc.error_message)
        self.assertGreater(tc.duration, 0)
    
    def test_test_case_execution_failure(self):
        """Test that TestCase handles assertion failures."""
        tc = TestCase("test_fail", "Should fail")
        
        def failing_test():
            assert False, "Expected failure"
        
        result = tc.execute(failing_test)
        
        self.assertEqual(result, TestResult.FAILED)
        self.assertEqual(tc.result, TestResult.FAILED)
        self.assertIn("Expected failure", tc.error_message)
    
    def test_test_case_execution_error(self):
        """Test that TestCase handles exceptions."""
        tc = TestCase("test_error", "Should error")
        
        def error_test():
            raise ValueError("Unexpected error")
        
        result = tc.execute(error_test)
        
        self.assertEqual(result, TestResult.ERROR)
        self.assertEqual(tc.result, TestResult.ERROR)
        self.assertIn("ValueError", tc.error_message)
    
    def test_test_case_to_dict(self):
        """Test that TestCase converts to dictionary correctly."""
        tc = TestCase("test_name", "description", ["tag1"])
        tc.execute(lambda: None)
        
        tc_dict = tc.to_dict()
        
        self.assertEqual(tc_dict["name"], "test_name")
        self.assertEqual(tc_dict["description"], "description")
        self.assertEqual(tc_dict["tags"], ["tag1"])
        self.assertIsNotNone(tc_dict["result"])


class TestTestSuite(unittest.TestCase):
    """Unit tests for TestSuite class."""
    
    def test_test_suite_initialization(self):
        """Test that TestSuite initializes correctly."""
        suite = TestSuite("suite_name", "suite_description")
        
        self.assertEqual(suite.name, "suite_name")
        self.assertEqual(suite.description, "suite_description")
        self.assertEqual(len(suite.test_cases), 0)
    
    def test_add_test(self):
        """Test adding tests to suite."""
        suite = TestSuite("suite")
        tc1 = TestCase("test1")
        tc2 = TestCase("test2")
        
        suite.add_test(tc1)
        suite.add_test(tc2)
        
        self.assertEqual(len(suite.test_cases), 2)
        self.assertIn(tc1, suite.test_cases)
        self.assertIn(tc2, suite.test_cases)
    
    def test_run_suite(self):
        """Test running a test suite."""
        suite = TestSuite("test_suite")
        
        tc1 = TestCase("test1")
        tc1.execute(lambda: None)
        suite.add_test(tc1)
        
        tc2 = TestCase("test2")
        tc2.execute(lambda: (_ for _ in ()).throw(AssertionError("fail")))
        suite.add_test(tc2)
        
        results = suite.run()
        
        self.assertEqual(results["suite_name"], "test_suite")
        self.assertIsNotNone(results["start_time"])
        self.assertIsNotNone(results["end_time"])
        self.assertEqual(results["total_tests"], 2)
    
    def test_get_summary(self):
        """Test getting suite summary."""
        suite = TestSuite("test_suite")
        
        tc = TestCase("test1")
        tc.execute(lambda: None)
        suite.add_test(tc)
        
        suite.run()
        summary = suite.get_summary()
        
        self.assertIn("test_suite", summary)
        self.assertIn("Total Tests:", summary)
        self.assertIn("Passed:", summary)


class TestCustomAssertions(unittest.TestCase):
    """Unit tests for CustomAssertions class."""
    
    def test_assert_in_range_success(self):
        """Test assert_in_range with value in range."""
        # Should not raise exception
        CustomAssertions.assert_in_range(5, 1, 10)
        CustomAssertions.assert_in_range(1, 1, 10)
        CustomAssertions.assert_in_range(10, 1, 10)
    
    def test_assert_in_range_failure(self):
        """Test assert_in_range with value out of range."""
        with self.assertRaises(AssertionError):
            CustomAssertions.assert_in_range(0, 1, 10)
        
        with self.assertRaises(AssertionError):
            CustomAssertions.assert_in_range(11, 1, 10)
    
    def test_assert_dict_contains_success(self):
        """Test assert_dict_contains with all keys present."""
        test_dict = {"a": 1, "b": 2, "c": 3}
        CustomAssertions.assert_dict_contains(test_dict, ["a", "b"])
    
    def test_assert_dict_contains_failure(self):
        """Test assert_dict_contains with missing keys."""
        test_dict = {"a": 1, "b": 2}
        
        with self.assertRaises(AssertionError) as ctx:
            CustomAssertions.assert_dict_contains(test_dict, ["a", "c"])
        
        self.assertIn("missing keys", str(ctx.exception))
    
    def test_assert_list_contains_success(self):
        """Test assert_list_contains with all items present."""
        test_list = [1, 2, 3, 4]
        CustomAssertions.assert_list_contains(test_list, [1, 3])
    
    def test_assert_list_contains_failure(self):
        """Test assert_list_contains with missing items."""
        test_list = [1, 2, 3]
        
        with self.assertRaises(AssertionError) as ctx:
            CustomAssertions.assert_list_contains(test_list, [1, 4])
        
        self.assertIn("missing items", str(ctx.exception))
    
    def test_assert_response_time_success(self):
        """Test assert_response_time with acceptable duration."""
        CustomAssertions.assert_response_time(0.5, 1.0)
    
    def test_assert_response_time_failure(self):
        """Test assert_response_time with excessive duration."""
        with self.assertRaises(AssertionError) as ctx:
            CustomAssertions.assert_response_time(2.0, 1.0)
        
        self.assertIn("exceeds maximum", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()

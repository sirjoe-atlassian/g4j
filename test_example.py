#!/usr/bin/env python3
"""
Example test cases demonstrating the test automation framework.
"""

import unittest
from test_automation import BaseTestCase


class ExampleTestCase(BaseTestCase):
    """Example test case class."""
    
    def test_addition(self):
        """Test basic addition operation."""
        result = 2 + 2
        self.assertEqual(result, 4, "Addition test failed")
    
    def test_string_operations(self):
        """Test string operations."""
        text = "hello world"
        self.assert_contains(text, "hello", "String should contain 'hello'")
        self.assertTrue(text.startswith("hello"), "String should start with 'hello'")
    
    def test_list_operations(self):
        """Test list operations."""
        test_list = [1, 2, 3, 4, 5]
        self.assertEqual(len(test_list), 5, "List should have 5 elements")
        self.assert_contains(test_list, 3, "List should contain 3")
    
    def test_dictionary_operations(self):
        """Test dictionary operations."""
        test_dict = {'key1': 'value1', 'key2': 'value2'}
        self.assertIn('key1', test_dict, "Dictionary should contain 'key1'")
        self.assertEqual(test_dict['key1'], 'value1', "Value should be 'value1'")


class ExampleAPITestCase(BaseTestCase):
    """Example API test case class."""
    
    def test_response_code_success(self):
        """Test successful response code."""
        # Simulating a 200 OK response
        response_code = 200
        self.assert_response_code(response_code, 200, "API should return 200 OK")
    
    def test_response_code_not_found(self):
        """Test not found response code."""
        # Simulating a 404 response
        response_code = 404
        self.assert_response_code(response_code, 404, "API should return 404 Not Found")


if __name__ == "__main__":
    unittest.main(verbosity=2)

#!/usr/bin/env python3
"""
Example Test Suite
This module contains example test cases demonstrating the test automation framework.
"""

import unittest


class TestMathOperations(unittest.TestCase):
    """Test cases for basic math operations."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.a = 10
        self.b = 5
    
    def tearDown(self):
        """Clean up after each test method."""
        pass
    
    def test_addition(self):
        """Test addition operation."""
        result = self.a + self.b
        self.assertEqual(result, 15, "Addition should return correct sum")
    
    def test_subtraction(self):
        """Test subtraction operation."""
        result = self.a - self.b
        self.assertEqual(result, 5, "Subtraction should return correct difference")
    
    def test_multiplication(self):
        """Test multiplication operation."""
        result = self.a * self.b
        self.assertEqual(result, 50, "Multiplication should return correct product")
    
    def test_division(self):
        """Test division operation."""
        result = self.a / self.b
        self.assertEqual(result, 2.0, "Division should return correct quotient")
    
    def test_division_by_zero(self):
        """Test division by zero raises exception."""
        with self.assertRaises(ZeroDivisionError):
            result = self.a / 0


class TestStringOperations(unittest.TestCase):
    """Test cases for string operations."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_string = "Hello, World!"
    
    def test_string_length(self):
        """Test string length."""
        self.assertEqual(len(self.test_string), 13, "String length should be 13")
    
    def test_string_upper(self):
        """Test string uppercase conversion."""
        result = self.test_string.upper()
        self.assertEqual(result, "HELLO, WORLD!", "String should be uppercase")
    
    def test_string_lower(self):
        """Test string lowercase conversion."""
        result = self.test_string.lower()
        self.assertEqual(result, "hello, world!", "String should be lowercase")
    
    def test_string_contains(self):
        """Test string contains substring."""
        self.assertIn("World", self.test_string, "String should contain 'World'")
    
    def test_string_startswith(self):
        """Test string starts with prefix."""
        self.assertTrue(self.test_string.startswith("Hello"), 
                       "String should start with 'Hello'")


class TestListOperations(unittest.TestCase):
    """Test cases for list operations."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_list = [1, 2, 3, 4, 5]
    
    def test_list_length(self):
        """Test list length."""
        self.assertEqual(len(self.test_list), 5, "List should have 5 elements")
    
    def test_list_append(self):
        """Test list append operation."""
        self.test_list.append(6)
        self.assertEqual(len(self.test_list), 6, "List should have 6 elements after append")
        self.assertEqual(self.test_list[-1], 6, "Last element should be 6")
    
    def test_list_remove(self):
        """Test list remove operation."""
        self.test_list.remove(3)
        self.assertNotIn(3, self.test_list, "List should not contain 3 after removal")
    
    def test_list_index(self):
        """Test list index operation."""
        index = self.test_list.index(3)
        self.assertEqual(index, 2, "Element 3 should be at index 2")
    
    def test_list_sort(self):
        """Test list sort operation."""
        unsorted_list = [5, 2, 8, 1, 9]
        unsorted_list.sort()
        self.assertEqual(unsorted_list, [1, 2, 5, 8, 9], "List should be sorted")


if __name__ == '__main__':
    unittest.main()

"""
Example test automation module for g4j project.
This module demonstrates basic test automation structure.
"""

import unittest


class TestExample(unittest.TestCase):
    """Example test case class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        pass
    
    def tearDown(self):
        """Clean up after each test method."""
        pass
    
    def test_example_pass(self):
        """Test case that should pass."""
        self.assertEqual(1 + 1, 2)
    
    def test_string_operations(self):
        """Test string operations."""
        test_string = "g4j"
        self.assertEqual(test_string.upper(), "G4J")
        self.assertTrue(test_string.startswith("g"))
    
    def test_list_operations(self):
        """Test list operations."""
        test_list = [1, 2, 3]
        self.assertIn(2, test_list)
        self.assertEqual(len(test_list), 3)


if __name__ == '__main__':
    unittest.main()

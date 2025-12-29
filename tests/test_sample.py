"""
Sample test automation code for g4j project.
This demonstrates basic test structure and patterns.
"""

import unittest


class TestSample(unittest.TestCase):
    """Sample test class demonstrating test automation structure."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_data = {"key": "value"}

    def tearDown(self):
        """Clean up after each test method."""
        self.test_data = None

    def test_basic_assertion(self):
        """Test basic assertion functionality."""
        self.assertEqual(1 + 1, 2)
        self.assertTrue(True)
        self.assertFalse(False)

    def test_string_operations(self):
        """Test string manipulation operations."""
        text = "Hello, World!"
        self.assertIn("World", text)
        self.assertEqual(text.lower(), "hello, world!")
        self.assertEqual(len(text), 13)

    def test_list_operations(self):
        """Test list operations and assertions."""
        test_list = [1, 2, 3, 4, 5]
        self.assertEqual(len(test_list), 5)
        self.assertIn(3, test_list)
        self.assertEqual(test_list[0], 1)
        self.assertEqual(test_list[-1], 5)

    def test_dictionary_operations(self):
        """Test dictionary operations."""
        self.assertIsNotNone(self.test_data)
        self.assertIn("key", self.test_data)
        self.assertEqual(self.test_data["key"], "value")


class TestAdvanced(unittest.TestCase):
    """Advanced test examples with more complex scenarios."""

    def test_exception_handling(self):
        """Test that exceptions are raised correctly."""
        with self.assertRaises(ValueError):
            raise ValueError("Expected error")

    def test_with_subtest(self):
        """Test using subtests for multiple assertions."""
        test_cases = [
            (1, 1, 2),
            (2, 3, 5),
            (10, 5, 15),
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(a + b, expected)


if __name__ == '__main__':
    unittest.main()

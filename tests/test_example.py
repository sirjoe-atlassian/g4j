"""
Test automation example for g4j project.
This module provides sample test cases demonstrating test automation patterns.
"""

import unittest


class TestExample(unittest.TestCase):
    """Example test class demonstrating basic test automation."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_data = {"key": "value", "number": 42}

    def tearDown(self):
        """Clean up after each test method."""
        self.test_data = None

    def test_basic_assertion(self):
        """Test basic assertion functionality."""
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertEqual(1 + 1, 2)

    def test_data_structure(self):
        """Test data structure operations."""
        self.assertIn("key", self.test_data)
        self.assertEqual(self.test_data["key"], "value")
        self.assertEqual(self.test_data["number"], 42)

    def test_string_operations(self):
        """Test string manipulation operations."""
        test_string = "Hello, World!"
        self.assertIn("World", test_string)
        self.assertTrue(test_string.startswith("Hello"))
        self.assertEqual(test_string.lower(), "hello, world!")

    def test_list_operations(self):
        """Test list operations."""
        test_list = [1, 2, 3, 4, 5]
        self.assertEqual(len(test_list), 5)
        self.assertIn(3, test_list)
        self.assertEqual(test_list[0], 1)
        self.assertEqual(test_list[-1], 5)

    def test_exception_handling(self):
        """Test exception handling."""
        with self.assertRaises(ZeroDivisionError):
            _ = 1 / 0

        with self.assertRaises(KeyError):
            _ = self.test_data["nonexistent_key"]


class TestAdvancedExample(unittest.TestCase):
    """Advanced test examples with more complex scenarios."""

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures before any test methods run."""
        cls.shared_resource = "Shared test resource"

    @classmethod
    def tearDownClass(cls):
        """Clean up class-level fixtures after all test methods complete."""
        cls.shared_resource = None

    def test_shared_resource(self):
        """Test using shared class-level resource."""
        self.assertIsNotNone(self.shared_resource)
        self.assertEqual(self.shared_resource, "Shared test resource")

    def test_multiple_assertions(self):
        """Test with multiple related assertions."""
        result = {"status": "success", "code": 200, "data": [1, 2, 3]}
        
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["code"], 200)
        self.assertIsInstance(result["data"], list)
        self.assertEqual(len(result["data"]), 3)

    def test_subtest_example(self):
        """Test using subtests for parameterized testing."""
        test_cases = [
            (1, 2, 3),
            (0, 0, 0),
            (-1, 1, 0),
            (10, 20, 30)
        ]
        
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(a + b, expected)


def run_tests():
    """Run all test suites."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestExample))
    suite.addTests(loader.loadTestsFromTestCase(TestAdvancedExample))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result


if __name__ == "__main__":
    unittest.main()

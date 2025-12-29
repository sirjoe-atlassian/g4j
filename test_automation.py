"""
Test Automation Framework
DEV-4: Test automation generate code

This module provides a basic test automation framework with common utilities
for automated testing.
"""

import unittest
from typing import Any, Callable, List, Optional
import time


class TestBase(unittest.TestCase):
    """Base test class with common setup and teardown methods."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.start_time = time.time()
        print(f"\n--- Starting test: {self.id()} ---")
    
    def tearDown(self):
        """Clean up after each test method."""
        duration = time.time() - self.start_time
        print(f"--- Test completed in {duration:.2f}s ---")
    
    def assert_response_time(self, func: Callable, max_seconds: float, *args, **kwargs):
        """Assert that a function executes within the specified time."""
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        self.assertLessEqual(
            duration, 
            max_seconds, 
            f"Function took {duration:.2f}s, expected <= {max_seconds}s"
        )
        return result


class TestDataGenerator:
    """Utility class for generating test data."""
    
    @staticmethod
    def generate_user_data(count: int = 1) -> List[dict]:
        """Generate sample user data for testing.
        
        Args:
            count: Number of user records to generate
            
        Returns:
            List of user dictionaries with test data
        """
        users = []
        for i in range(count):
            users.append({
                "id": i + 1,
                "username": f"testuser{i + 1}",
                "email": f"testuser{i + 1}@example.com",
                "first_name": f"Test{i + 1}",
                "last_name": f"User{i + 1}",
                "active": True
            })
        return users
    
    @staticmethod
    def generate_product_data(count: int = 1) -> List[dict]:
        """Generate sample product data for testing.
        
        Args:
            count: Number of product records to generate
            
        Returns:
            List of product dictionaries with test data
        """
        products = []
        for i in range(count):
            products.append({
                "id": i + 1,
                "name": f"Test Product {i + 1}",
                "description": f"Description for test product {i + 1}",
                "price": (i + 1) * 10.0,
                "in_stock": True,
                "quantity": (i + 1) * 5
            })
        return products


class TestAssertion:
    """Custom assertion utilities for test automation."""
    
    @staticmethod
    def assert_dict_contains(actual: dict, expected: dict, message: Optional[str] = None):
        """Assert that actual dictionary contains all key-value pairs from expected.
        
        Args:
            actual: The dictionary to check
            expected: Dictionary containing expected key-value pairs
            message: Optional custom error message
        """
        for key, value in expected.items():
            if key not in actual:
                raise AssertionError(
                    message or f"Key '{key}' not found in actual dictionary"
                )
            if actual[key] != value:
                raise AssertionError(
                    message or f"Value mismatch for key '{key}': "
                    f"expected {value}, got {actual[key]}"
                )
    
    @staticmethod
    def assert_list_contains_item(items: List[Any], predicate: Callable[[Any], bool], 
                                   message: Optional[str] = None):
        """Assert that list contains at least one item matching the predicate.
        
        Args:
            items: List to search
            predicate: Function that returns True for matching items
            message: Optional custom error message
        """
        if not any(predicate(item) for item in items):
            raise AssertionError(
                message or "No item in list matches the given predicate"
            )


class MockApiResponse:
    """Mock API response for testing API clients."""
    
    def __init__(self, status_code: int = 200, json_data: Optional[dict] = None, 
                 text: str = "", headers: Optional[dict] = None):
        """Initialize mock API response.
        
        Args:
            status_code: HTTP status code
            json_data: JSON response data
            text: Response text
            headers: Response headers
        """
        self.status_code = status_code
        self._json_data = json_data or {}
        self.text = text
        self.headers = headers or {}
    
    def json(self) -> dict:
        """Return JSON data."""
        return self._json_data
    
    def is_success(self) -> bool:
        """Check if response indicates success."""
        return 200 <= self.status_code < 300


# Example test suite
class ExampleTestSuite(TestBase):
    """Example test suite demonstrating the test automation framework."""
    
    def test_user_data_generation(self):
        """Test user data generation utility."""
        users = TestDataGenerator.generate_user_data(count=3)
        
        self.assertEqual(len(users), 3)
        self.assertEqual(users[0]["username"], "testuser1")
        self.assertEqual(users[0]["email"], "testuser1@example.com")
        self.assertTrue(users[0]["active"])
    
    def test_product_data_generation(self):
        """Test product data generation utility."""
        products = TestDataGenerator.generate_product_data(count=2)
        
        self.assertEqual(len(products), 2)
        self.assertEqual(products[0]["name"], "Test Product 1")
        self.assertEqual(products[0]["price"], 10.0)
        self.assertTrue(products[0]["in_stock"])
    
    def test_dict_contains_assertion(self):
        """Test custom dictionary assertion."""
        actual = {"id": 1, "name": "test", "value": 100}
        expected = {"id": 1, "name": "test"}
        
        # Should not raise
        TestAssertion.assert_dict_contains(actual, expected)
        
        # Should raise
        with self.assertRaises(AssertionError):
            TestAssertion.assert_dict_contains(actual, {"id": 2})
    
    def test_list_contains_assertion(self):
        """Test custom list assertion."""
        items = [{"id": 1, "name": "a"}, {"id": 2, "name": "b"}]
        
        # Should not raise
        TestAssertion.assert_list_contains_item(
            items, 
            lambda x: x["id"] == 2
        )
        
        # Should raise
        with self.assertRaises(AssertionError):
            TestAssertion.assert_list_contains_item(
                items, 
                lambda x: x["id"] == 3
            )
    
    def test_mock_api_response(self):
        """Test mock API response utility."""
        response = MockApiResponse(
            status_code=200,
            json_data={"message": "success", "data": [1, 2, 3]}
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_success())
        self.assertEqual(response.json()["message"], "success")
        self.assertEqual(len(response.json()["data"]), 3)


if __name__ == "__main__":
    # Run the example test suite
    unittest.main(verbosity=2)

"""
Tests demonstrating the use of test helper utilities.
"""

import pytest
from tests.utils.test_helpers import (
    retry_on_failure,
    wait_until,
    TestDataGenerator,
    AssertionHelper
)


class TestRetryDecorator:
    """Tests for retry decorator."""
    
    def test_retry_success_on_first_attempt(self):
        """Test function succeeds on first attempt."""
        call_count = {"count": 0}
        
        @retry_on_failure(max_attempts=3, delay=0.1)
        def successful_function():
            call_count["count"] += 1
            return "success"
        
        result = successful_function()
        assert result == "success"
        assert call_count["count"] == 1
    
    def test_retry_success_after_failures(self):
        """Test function succeeds after some failures."""
        call_count = {"count": 0}
        
        @retry_on_failure(max_attempts=3, delay=0.1)
        def eventually_successful():
            call_count["count"] += 1
            if call_count["count"] < 3:
                raise ValueError("Not yet")
            return "success"
        
        result = eventually_successful()
        assert result == "success"
        assert call_count["count"] == 3


class TestWaitUntil:
    """Tests for wait_until utility."""
    
    def test_wait_until_condition_met(self):
        """Test waiting until condition is met."""
        counter = {"value": 0}
        
        def increment_and_check():
            counter["value"] += 1
            return counter["value"] >= 3
        
        result = wait_until(increment_and_check, timeout=5.0, poll_interval=0.1)
        assert result is True
        assert counter["value"] >= 3
    
    def test_wait_until_timeout(self):
        """Test timeout when condition is never met."""
        def always_false():
            return False
        
        with pytest.raises(TimeoutError):
            wait_until(always_false, timeout=1.0, poll_interval=0.1)


class TestDataGeneratorTests:
    """Tests for TestDataGenerator utility."""
    
    def test_generate_single_user(self):
        """Test generating a single user."""
        users = TestDataGenerator.generate_user_data(count=1)
        assert len(users) == 1
        assert users[0]["id"] == 1
        assert "name" in users[0]
        assert "email" in users[0]
    
    def test_generate_multiple_users(self):
        """Test generating multiple users."""
        users = TestDataGenerator.generate_user_data(count=5)
        assert len(users) == 5
        assert users[0]["id"] == 1
        assert users[4]["id"] == 5
    
    def test_generate_items(self):
        """Test generating items."""
        items = TestDataGenerator.generate_item_data(count=3)
        assert len(items) == 3
        assert all("price" in item for item in items)
        assert items[0]["price"] == 10.0
        assert items[2]["price"] == 30.0


class TestAssertionHelper:
    """Tests for AssertionHelper utility."""
    
    @pytest.mark.parametrize("email,expected", [
        ("test@example.com", True),
        ("user.name@domain.co.uk", True),
        ("invalid.email", False),
        ("@example.com", False),
        ("test@", False),
    ])
    def test_email_validation(self, email, expected):
        """Test email validation."""
        result = AssertionHelper.assert_valid_email(email)
        assert result == expected
    
    @pytest.mark.parametrize("value,min_val,max_val,expected", [
        (5, 1, 10, True),
        (1, 1, 10, True),
        (10, 1, 10, True),
        (0, 1, 10, False),
        (11, 1, 10, False),
    ])
    def test_range_validation(self, value, min_val, max_val, expected):
        """Test range validation."""
        result = AssertionHelper.assert_in_range(value, min_val, max_val)
        assert result == expected
    
    def test_dict_contains_keys(self):
        """Test dictionary key validation."""
        test_dict = {"name": "Test", "id": 1, "active": True}
        
        assert AssertionHelper.assert_dict_contains_keys(
            test_dict, ["name", "id"]
        )
        assert not AssertionHelper.assert_dict_contains_keys(
            test_dict, ["name", "missing_key"]
        )

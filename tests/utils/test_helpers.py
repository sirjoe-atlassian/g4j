"""
Helper functions for test automation.
"""

import time
from typing import Callable, Any, Optional
from functools import wraps


def retry_on_failure(max_attempts: int = 3, delay: float = 1.0):
    """
    Decorator to retry a function on failure.
    
    Args:
        max_attempts: Maximum number of retry attempts.
        delay: Delay in seconds between retries.
    
    Returns:
        Decorated function that retries on failure.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        print(f"Attempt {attempt + 1} failed: {str(e)}. Retrying...")
                        time.sleep(delay)
                    else:
                        print(f"All {max_attempts} attempts failed.")
            raise last_exception
        return wrapper
    return decorator


def wait_until(
    condition: Callable[[], bool],
    timeout: float = 10.0,
    poll_interval: float = 0.5,
    error_message: Optional[str] = None
) -> bool:
    """
    Wait until a condition is met or timeout occurs.
    
    Args:
        condition: Callable that returns True when condition is met.
        timeout: Maximum time to wait in seconds.
        poll_interval: Time between condition checks in seconds.
        error_message: Custom error message if timeout occurs.
    
    Returns:
        True if condition is met, raises TimeoutError otherwise.
    
    Raises:
        TimeoutError: If condition is not met within timeout period.
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        if condition():
            return True
        time.sleep(poll_interval)
    
    message = error_message or f"Condition not met within {timeout} seconds"
    raise TimeoutError(message)


class TestDataGenerator:
    """Utility class for generating test data."""
    
    @staticmethod
    def generate_user_data(count: int = 1) -> list:
        """
        Generate mock user data.
        
        Args:
            count: Number of user records to generate.
        
        Returns:
            List of user dictionaries.
        """
        return [
            {
                "id": i + 1,
                "name": f"User {i + 1}",
                "email": f"user{i + 1}@example.com",
                "active": True
            }
            for i in range(count)
        ]
    
    @staticmethod
    def generate_item_data(count: int = 1) -> list:
        """
        Generate mock item data.
        
        Args:
            count: Number of item records to generate.
        
        Returns:
            List of item dictionaries.
        """
        return [
            {
                "id": i + 1,
                "name": f"Item {i + 1}",
                "price": (i + 1) * 10.0,
                "available": True
            }
            for i in range(count)
        ]


class AssertionHelper:
    """Helper class for common assertions."""
    
    @staticmethod
    def assert_valid_email(email: str) -> bool:
        """
        Validate email format.
        
        Args:
            email: Email string to validate.
        
        Returns:
            True if email is valid format.
        """
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def assert_in_range(value: float, min_val: float, max_val: float) -> bool:
        """
        Check if value is within range.
        
        Args:
            value: Value to check.
            min_val: Minimum value (inclusive).
            max_val: Maximum value (inclusive).
        
        Returns:
            True if value is in range.
        """
        return min_val <= value <= max_val
    
    @staticmethod
    def assert_dict_contains_keys(data: dict, required_keys: list) -> bool:
        """
        Check if dictionary contains all required keys.
        
        Args:
            data: Dictionary to check.
            required_keys: List of required keys.
        
        Returns:
            True if all required keys are present.
        """
        return all(key in data for key in required_keys)

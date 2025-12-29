"""
Pytest configuration and shared fixtures for test automation.
"""

import pytest
from typing import Generator


@pytest.fixture(scope="session")
def test_config() -> dict:
    """
    Provides test configuration for the entire test session.
    
    Returns:
        dict: Configuration dictionary containing test settings.
    """
    return {
        "project_name": "g4j",
        "environment": "test",
        "timeout": 30,
        "retry_count": 3,
    }


@pytest.fixture(scope="function")
def setup_teardown() -> Generator[None, None, None]:
    """
    Setup and teardown fixture for test functions.
    
    Yields:
        None: Control is yielded to the test function.
    """
    # Setup
    print("\n[SETUP] Preparing test environment...")
    
    yield
    
    # Teardown
    print("\n[TEARDOWN] Cleaning up test environment...")


@pytest.fixture(scope="function")
def mock_data() -> dict:
    """
    Provides mock data for testing.
    
    Returns:
        dict: Mock data dictionary.
    """
    return {
        "user": {
            "id": 1,
            "name": "Test User",
            "email": "test@example.com"
        },
        "items": [
            {"id": 1, "name": "Item 1", "value": 100},
            {"id": 2, "name": "Item 2", "value": 200},
            {"id": 3, "name": "Item 3", "value": 300},
        ]
    }

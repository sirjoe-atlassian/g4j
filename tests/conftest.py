"""
Pytest configuration file for test automation.
This file contains shared fixtures and configuration for pytest.
"""

import pytest


@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {
        "name": "Test User",
        "email": "test@example.com",
        "age": 30,
        "active": True
    }


@pytest.fixture
def sample_list():
    """Provide sample list for tests."""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@pytest.fixture(scope="session")
def session_data():
    """Provide session-scoped data that persists across all tests."""
    return {"session_id": "test_session_123"}


@pytest.fixture
def mock_api_response():
    """Provide mock API response for testing."""
    return {
        "status": 200,
        "data": {
            "id": 1,
            "title": "Test Item",
            "description": "This is a test item"
        },
        "message": "Success"
    }

"""
Pytest configuration and shared fixtures.
"""

import pytest


@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {
        'name': 'g4j',
        'version': '1.0.0',
        'description': 'Test automation project'
    }


@pytest.fixture
def sample_list():
    """Provide a sample list for tests."""
    return [1, 2, 3, 4, 5]


@pytest.fixture(scope='session')
def test_config():
    """Provide test configuration."""
    return {
        'environment': 'test',
        'debug': True
    }

"""Pytest configuration and fixtures."""
import pytest
from utils.api_client import APIClient
from utils.config_reader import config_reader
from utils.logger import logger


@pytest.fixture(scope='session')
def api_client():
    """Create API client for testing.
    
    Yields:
        APIClient instance
    """
    client = APIClient()
    logger.info("API client initialized")
    yield client
    client.close()
    logger.info("API client closed")


@pytest.fixture(scope='session')
def config():
    """Provide configuration reader.
    
    Returns:
        ConfigReader instance
    """
    return config_reader


@pytest.fixture(scope='function')
def test_logger():
    """Provide logger for tests.
    
    Returns:
        Logger instance
    """
    return logger


@pytest.fixture(autouse=True)
def log_test_info(request):
    """Log test information before and after each test."""
    logger.info(f"Starting test: {request.node.nodeid}")
    yield
    logger.info(f"Finished test: {request.node.nodeid}")


def pytest_configure(config):
    """Configure pytest."""
    config.addinivalue_line(
        "markers", "smoke: mark test as part of smoke test suite"
    )
    config.addinivalue_line(
        "markers", "regression: mark test as part of regression test suite"
    )

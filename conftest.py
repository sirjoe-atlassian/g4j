"""
Pytest configuration and fixtures
Jira Issue: DEV-4 - Test automation generate code
"""

import pytest
import logging
from typing import Dict, Any


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def test_config() -> Dict[str, Any]:
    """Provide test configuration"""
    return {
        'base_url': 'https://api.example.com',
        'timeout': 30,
        'retry_count': 3
    }


@pytest.fixture(scope="function")
def sample_user_data() -> Dict[str, Any]:
    """Provide sample user data for testing"""
    return {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'SecurePass123!',
        'active': True
    }


@pytest.fixture(scope="function")
def api_client(test_config):
    """Provide an API client instance"""
    class MockAPIClient:
        def __init__(self, config):
            self.base_url = config['base_url']
            self.timeout = config['timeout']
        
        def get(self, endpoint: str) -> Dict[str, Any]:
            """Mock GET request"""
            return {'status': 200, 'data': {}}
        
        def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
            """Mock POST request"""
            return {'status': 201, 'data': data}
    
    client = MockAPIClient(test_config)
    yield client
    # Cleanup if needed
    logger.info("API client cleanup completed")


@pytest.fixture(scope="function")
def browser_driver():
    """Provide a browser driver instance for UI tests"""
    # Mock browser driver - replace with actual Selenium WebDriver
    class MockDriver:
        def __init__(self):
            self.current_url = ""
        
        def get(self, url: str):
            self.current_url = url
        
        def quit(self):
            pass
    
    driver = MockDriver()
    yield driver
    driver.quit()
    logger.info("Browser driver cleanup completed")


@pytest.fixture(autouse=True)
def log_test_info(request):
    """Automatically log test information"""
    logger.info(f"Running test: {request.node.nodeid}")
    yield
    logger.info(f"Finished test: {request.node.nodeid}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test results"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call":
        if report.failed:
            logger.error(f"Test FAILED: {item.nodeid}")
        elif report.passed:
            logger.info(f"Test PASSED: {item.nodeid}")

"""
Pytest configuration and fixtures for test automation.
"""
import pytest
from src.config.config import Config
from src.utils.api_client import APIClient
from src.utils.logger import setup_logger

logger = setup_logger()

# Try to import selenium, but make it optional
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False
    logger.warning("Selenium not installed. Web UI tests will be skipped.")


@pytest.fixture(scope='session')
def config():
    """Provide configuration object."""
    return Config()


@pytest.fixture(scope='session')
def api_client(config):
    """Provide API client instance."""
    client = APIClient(config.API_BASE_URL, config.API_TIMEOUT)
    yield client
    client.close()


@pytest.fixture(scope='function')
def browser(config):
    """Provide browser instance for web testing."""
    if not SELENIUM_AVAILABLE:
        pytest.skip("Selenium is not installed")
    
    driver = None
    
    try:
        if config.BROWSER.lower() == 'chrome':
            options = ChromeOptions()
            if config.HEADLESS:
                options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(options=options)
        elif config.BROWSER.lower() == 'firefox':
            options = FirefoxOptions()
            if config.HEADLESS:
                options.add_argument('--headless')
            driver = webdriver.Firefox(options=options)
        else:
            raise ValueError(f'Unsupported browser: {config.BROWSER}')
        
        driver.implicitly_wait(config.IMPLICIT_WAIT)
        driver.maximize_window()
        
        yield driver
        
    finally:
        if driver:
            driver.quit()


@pytest.fixture(scope='function')
def screenshot_on_failure(request, browser):
    """Take screenshot on test failure."""
    yield
    
    if request.node.rep_call.failed if hasattr(request.node, 'rep_call') else False:
        screenshot_path = f'screenshots/{request.node.name}.png'
        import os
        os.makedirs('screenshots', exist_ok=True)
        browser.save_screenshot(screenshot_path)
        logger.info(f'Screenshot saved: {screenshot_path}')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test results for fixtures."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f'rep_{rep.when}', rep)


def pytest_configure(config):
    """Configure pytest with custom markers and settings."""
    config.addinivalue_line('markers', 'smoke: Smoke test cases')
    config.addinivalue_line('markers', 'regression: Regression test cases')
    config.addinivalue_line('markers', 'integration: Integration test cases')
    config.addinivalue_line('markers', 'unit: Unit test cases')

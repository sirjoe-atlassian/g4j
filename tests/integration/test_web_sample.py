"""
Sample web UI tests for test automation framework.
These are example tests that can be customized for your application.
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.integration
class TestGoogleSearch:
    """
    Sample web tests using Google as an example.
    Replace with your actual application tests.
    """
    
    def test_google_homepage_loads(self, browser):
        """Test that Google homepage loads successfully."""
        browser.get('https://www.google.com')
        assert 'Google' in browser.title
    
    def test_google_search_box_exists(self, browser):
        """Test that search box is present on homepage."""
        browser.get('https://www.google.com')
        search_box = browser.find_element(By.NAME, 'q')
        assert search_box is not None
        assert search_box.is_displayed()


@pytest.mark.smoke
class TestBasicWebNavigation:
    """Test basic web navigation functionality."""
    
    def test_navigate_to_url(self, browser):
        """Test navigating to a URL."""
        browser.get('https://www.example.com')
        assert 'example' in browser.current_url.lower()
    
    def test_page_title(self, browser):
        """Test getting page title."""
        browser.get('https://www.example.com')
        title = browser.title
        assert title is not None
        assert len(title) > 0
    
    def test_get_page_source(self, browser):
        """Test getting page source."""
        browser.get('https://www.example.com')
        page_source = browser.page_source
        assert page_source is not None
        assert len(page_source) > 0
        assert 'Example Domain' in page_source

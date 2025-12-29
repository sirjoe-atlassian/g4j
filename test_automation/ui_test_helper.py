#!/usr/bin/env python3
"""
UI Test Helper
This module provides helper functions for UI testing automation using Selenium.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from typing import Optional, List


class UITestHelper:
    """Helper class for UI testing automation."""
    
    def __init__(self, browser: str = 'chrome', headless: bool = False):
        """
        Initialize UI test helper.
        
        Args:
            browser (str): Browser to use ('chrome', 'firefox', 'edge')
            headless (bool): Run browser in headless mode
        """
        self.browser = browser.lower()
        self.headless = headless
        self.driver = None
        self.default_timeout = 10
    
    def start_browser(self):
        """Start the browser."""
        if self.browser == 'chrome':
            options = webdriver.ChromeOptions()
            if self.headless:
                options.add_argument('--headless')
            self.driver = webdriver.Chrome(options=options)
        elif self.browser == 'firefox':
            options = webdriver.FirefoxOptions()
            if self.headless:
                options.add_argument('--headless')
            self.driver = webdriver.Firefox(options=options)
        elif self.browser == 'edge':
            options = webdriver.EdgeOptions()
            if self.headless:
                options.add_argument('--headless')
            self.driver = webdriver.Edge(options=options)
        else:
            raise ValueError(f"Unsupported browser: {self.browser}")
        
        self.driver.maximize_window()
    
    def stop_browser(self):
        """Stop the browser."""
        if self.driver:
            self.driver.quit()
            self.driver = None
    
    def navigate_to(self, url: str):
        """
        Navigate to URL.
        
        Args:
            url (str): URL to navigate to
        """
        if not self.driver:
            self.start_browser()
        self.driver.get(url)
    
    def find_element(self, locator: str, by: By = By.CSS_SELECTOR, 
                    timeout: Optional[int] = None) -> webdriver.remote.webelement.WebElement:
        """
        Find element with wait.
        
        Args:
            locator (str): Element locator
            by (By): Locator strategy
            timeout (int): Timeout in seconds
            
        Returns:
            WebElement: Found element
        """
        timeout = timeout or self.default_timeout
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.presence_of_element_located((by, locator)))
        return element
    
    def find_elements(self, locator: str, by: By = By.CSS_SELECTOR) -> List[webdriver.remote.webelement.WebElement]:
        """
        Find multiple elements.
        
        Args:
            locator (str): Element locator
            by (By): Locator strategy
            
        Returns:
            List[WebElement]: Found elements
        """
        return self.driver.find_elements(by, locator)
    
    def click_element(self, locator: str, by: By = By.CSS_SELECTOR, timeout: Optional[int] = None):
        """
        Click element.
        
        Args:
            locator (str): Element locator
            by (By): Locator strategy
            timeout (int): Timeout in seconds
        """
        element = self.find_element(locator, by, timeout)
        element.click()
    
    def enter_text(self, locator: str, text: str, by: By = By.CSS_SELECTOR, 
                  timeout: Optional[int] = None, clear_first: bool = True):
        """
        Enter text into element.
        
        Args:
            locator (str): Element locator
            text (str): Text to enter
            by (By): Locator strategy
            timeout (int): Timeout in seconds
            clear_first (bool): Clear field before entering text
        """
        element = self.find_element(locator, by, timeout)
        if clear_first:
            element.clear()
        element.send_keys(text)
    
    def get_text(self, locator: str, by: By = By.CSS_SELECTOR, timeout: Optional[int] = None) -> str:
        """
        Get element text.
        
        Args:
            locator (str): Element locator
            by (By): Locator strategy
            timeout (int): Timeout in seconds
            
        Returns:
            str: Element text
        """
        element = self.find_element(locator, by, timeout)
        return element.text
    
    def is_element_visible(self, locator: str, by: By = By.CSS_SELECTOR, 
                          timeout: Optional[int] = None) -> bool:
        """
        Check if element is visible.
        
        Args:
            locator (str): Element locator
            by (By): Locator strategy
            timeout (int): Timeout in seconds
            
        Returns:
            bool: True if visible, False otherwise
        """
        timeout = timeout or self.default_timeout
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located((by, locator)))
            return True
        except TimeoutException:
            return False
    
    def wait_for_element_to_disappear(self, locator: str, by: By = By.CSS_SELECTOR, 
                                     timeout: Optional[int] = None):
        """
        Wait for element to disappear.
        
        Args:
            locator (str): Element locator
            by (By): Locator strategy
            timeout (int): Timeout in seconds
        """
        timeout = timeout or self.default_timeout
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.invisibility_of_element_located((by, locator)))
    
    def take_screenshot(self, filename: str):
        """
        Take screenshot.
        
        Args:
            filename (str): Screenshot filename
        """
        self.driver.save_screenshot(filename)
    
    def get_current_url(self) -> str:
        """
        Get current URL.
        
        Returns:
            str: Current URL
        """
        return self.driver.current_url
    
    def get_page_title(self) -> str:
        """
        Get page title.
        
        Returns:
            str: Page title
        """
        return self.driver.title

"""
Configuration management for test automation framework.
"""
import os
from typing import Dict, Any


class Config:
    """Base configuration class."""
    
    # API Configuration
    API_BASE_URL = os.getenv('API_BASE_URL', 'https://api.example.com')
    API_TIMEOUT = int(os.getenv('API_TIMEOUT', '30'))
    
    # Web Configuration
    WEB_BASE_URL = os.getenv('WEB_BASE_URL', 'https://www.example.com')
    BROWSER = os.getenv('BROWSER', 'chrome')
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'
    IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', '10'))
    
    # Test Configuration
    PARALLEL_WORKERS = int(os.getenv('PARALLEL_WORKERS', '4'))
    SCREENSHOT_ON_FAILURE = os.getenv('SCREENSHOT_ON_FAILURE', 'true').lower() == 'true'
    
    # Reporting
    REPORT_PATH = os.getenv('REPORT_PATH', 'reports')
    ALLURE_RESULTS = os.getenv('ALLURE_RESULTS', 'allure-results')
    
    @classmethod
    def get_config(cls) -> Dict[str, Any]:
        """Get all configuration as dictionary."""
        return {
            'api_base_url': cls.API_BASE_URL,
            'api_timeout': cls.API_TIMEOUT,
            'web_base_url': cls.WEB_BASE_URL,
            'browser': cls.BROWSER,
            'headless': cls.HEADLESS,
            'implicit_wait': cls.IMPLICIT_WAIT,
            'parallel_workers': cls.PARALLEL_WORKERS,
            'screenshot_on_failure': cls.SCREENSHOT_ON_FAILURE,
            'report_path': cls.REPORT_PATH,
            'allure_results': cls.ALLURE_RESULTS,
        }

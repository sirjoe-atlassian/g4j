"""
Test Automation Framework
A comprehensive test automation framework for API and UI testing.
"""

__version__ = '1.0.0'
__author__ = 'Test Automation Team'

from .test_runner import TestRunner
from .api_test_helper import APITestHelper
from .ui_test_helper import UITestHelper

__all__ = ['TestRunner', 'APITestHelper', 'UITestHelper']

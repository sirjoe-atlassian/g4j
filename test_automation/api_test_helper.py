#!/usr/bin/env python3
"""
API Test Helper
This module provides helper functions for API testing automation.
"""

import json
import requests
from typing import Dict, Any, Optional


class APITestHelper:
    """Helper class for API testing automation."""
    
    def __init__(self, base_url: str, default_headers: Optional[Dict[str, str]] = None):
        """
        Initialize API test helper.
        
        Args:
            base_url (str): Base URL for API endpoints
            default_headers (dict): Default headers to include in requests
        """
        self.base_url = base_url.rstrip('/')
        self.default_headers = default_headers or {}
        self.session = requests.Session()
        self.session.headers.update(self.default_headers)
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None, 
            headers: Optional[Dict[str, str]] = None) -> requests.Response:
        """
        Perform GET request.
        
        Args:
            endpoint (str): API endpoint
            params (dict): Query parameters
            headers (dict): Additional headers
            
        Returns:
            requests.Response: Response object
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.get(url, params=params, headers=headers)
        return response
    
    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None,
             json_data: Optional[Dict[str, Any]] = None,
             headers: Optional[Dict[str, str]] = None) -> requests.Response:
        """
        Perform POST request.
        
        Args:
            endpoint (str): API endpoint
            data (dict): Form data
            json_data (dict): JSON data
            headers (dict): Additional headers
            
        Returns:
            requests.Response: Response object
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.post(url, data=data, json=json_data, headers=headers)
        return response
    
    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None,
            json_data: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None) -> requests.Response:
        """
        Perform PUT request.
        
        Args:
            endpoint (str): API endpoint
            data (dict): Form data
            json_data (dict): JSON data
            headers (dict): Additional headers
            
        Returns:
            requests.Response: Response object
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.put(url, data=data, json=json_data, headers=headers)
        return response
    
    def delete(self, endpoint: str, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        """
        Perform DELETE request.
        
        Args:
            endpoint (str): API endpoint
            headers (dict): Additional headers
            
        Returns:
            requests.Response: Response object
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.delete(url, headers=headers)
        return response
    
    def assert_status_code(self, response: requests.Response, expected_code: int):
        """
        Assert response status code.
        
        Args:
            response (requests.Response): Response object
            expected_code (int): Expected status code
            
        Raises:
            AssertionError: If status code doesn't match
        """
        assert response.status_code == expected_code, \
            f"Expected status code {expected_code}, got {response.status_code}"
    
    def assert_response_contains(self, response: requests.Response, key: str):
        """
        Assert response JSON contains key.
        
        Args:
            response (requests.Response): Response object
            key (str): Key to check for
            
        Raises:
            AssertionError: If key not found
        """
        json_data = response.json()
        assert key in json_data, f"Response does not contain key: {key}"
    
    def assert_response_value(self, response: requests.Response, key: str, expected_value: Any):
        """
        Assert response JSON value matches expected.
        
        Args:
            response (requests.Response): Response object
            key (str): Key to check
            expected_value: Expected value
            
        Raises:
            AssertionError: If value doesn't match
        """
        json_data = response.json()
        actual_value = json_data.get(key)
        assert actual_value == expected_value, \
            f"Expected {key}={expected_value}, got {actual_value}"

"""
API client utilities for test automation.
"""
import requests
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


class APIClient:
    """HTTP API client for testing."""
    
    def __init__(self, base_url: str, timeout: int = 30):
        """
        Initialize API client.
        
        Args:
            base_url: Base URL for API requests
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        self.headers = {'Content-Type': 'application/json'}
    
    def set_auth_token(self, token: str, token_type: str = 'Bearer'):
        """Set authentication token."""
        self.headers['Authorization'] = f'{token_type} {token}'
    
    def get(self, endpoint: str, params: Optional[Dict] = None, 
            headers: Optional[Dict] = None) -> requests.Response:
        """Send GET request."""
        url = f'{self.base_url}/{endpoint.lstrip("/")}'
        merged_headers = {**self.headers, **(headers or {})}
        
        logger.info(f'GET {url}')
        response = self.session.get(url, params=params, headers=merged_headers, 
                                    timeout=self.timeout)
        logger.info(f'Response: {response.status_code}')
        return response
    
    def post(self, endpoint: str, data: Optional[Dict] = None, 
             json: Optional[Dict] = None, headers: Optional[Dict] = None) -> requests.Response:
        """Send POST request."""
        url = f'{self.base_url}/{endpoint.lstrip("/")}'
        merged_headers = {**self.headers, **(headers or {})}
        
        logger.info(f'POST {url}')
        response = self.session.post(url, data=data, json=json, 
                                     headers=merged_headers, timeout=self.timeout)
        logger.info(f'Response: {response.status_code}')
        return response
    
    def put(self, endpoint: str, data: Optional[Dict] = None,
            json: Optional[Dict] = None, headers: Optional[Dict] = None) -> requests.Response:
        """Send PUT request."""
        url = f'{self.base_url}/{endpoint.lstrip("/")}'
        merged_headers = {**self.headers, **(headers or {})}
        
        logger.info(f'PUT {url}')
        response = self.session.put(url, data=data, json=json, 
                                    headers=merged_headers, timeout=self.timeout)
        logger.info(f'Response: {response.status_code}')
        return response
    
    def delete(self, endpoint: str, headers: Optional[Dict] = None) -> requests.Response:
        """Send DELETE request."""
        url = f'{self.base_url}/{endpoint.lstrip("/")}'
        merged_headers = {**self.headers, **(headers or {})}
        
        logger.info(f'DELETE {url}')
        response = self.session.delete(url, headers=merged_headers, timeout=self.timeout)
        logger.info(f'Response: {response.status_code}')
        return response
    
    def close(self):
        """Close the session."""
        self.session.close()

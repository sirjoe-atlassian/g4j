"""API client utility for making HTTP requests."""
import requests
from typing import Dict, Optional, Any
from utils.logger import logger
from utils.config_reader import config_reader


class APIClient:
    """HTTP client for API testing."""
    
    def __init__(self, base_url: Optional[str] = None):
        """Initialize the API client.
        
        Args:
            base_url: Base URL for API requests. If None, reads from config.
        """
        self.base_url = base_url or config_reader.get_base_url()
        self.timeout = config_reader.get_timeout()
        self.session = requests.Session()
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    
    def set_auth_token(self, token: str):
        """Set authorization token for requests.
        
        Args:
            token: Bearer token for authentication
        """
        self.headers['Authorization'] = f'Bearer {token}'
    
    def get(self, endpoint: str, params: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Send GET request.
        
        Args:
            endpoint: API endpoint
            params: Query parameters
            **kwargs: Additional arguments for requests
            
        Returns:
            Response object
        """
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET request to: {url}")
        
        response = self.session.get(
            url,
            params=params,
            headers=self.headers,
            timeout=self.timeout,
            **kwargs
        )
        
        logger.info(f"Response status: {response.status_code}")
        return response
    
    def post(self, endpoint: str, data: Optional[Dict] = None, 
             json: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Send POST request.
        
        Args:
            endpoint: API endpoint
            data: Form data
            json: JSON data
            **kwargs: Additional arguments for requests
            
        Returns:
            Response object
        """
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST request to: {url}")
        
        response = self.session.post(
            url,
            data=data,
            json=json,
            headers=self.headers,
            timeout=self.timeout,
            **kwargs
        )
        
        logger.info(f"Response status: {response.status_code}")
        return response
    
    def put(self, endpoint: str, data: Optional[Dict] = None,
            json: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Send PUT request.
        
        Args:
            endpoint: API endpoint
            data: Form data
            json: JSON data
            **kwargs: Additional arguments for requests
            
        Returns:
            Response object
        """
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT request to: {url}")
        
        response = self.session.put(
            url,
            data=data,
            json=json,
            headers=self.headers,
            timeout=self.timeout,
            **kwargs
        )
        
        logger.info(f"Response status: {response.status_code}")
        return response
    
    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """Send DELETE request.
        
        Args:
            endpoint: API endpoint
            **kwargs: Additional arguments for requests
            
        Returns:
            Response object
        """
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE request to: {url}")
        
        response = self.session.delete(
            url,
            headers=self.headers,
            timeout=self.timeout,
            **kwargs
        )
        
        logger.info(f"Response status: {response.status_code}")
        return response
    
    def close(self):
        """Close the session."""
        self.session.close()

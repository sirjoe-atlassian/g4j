#!/usr/bin/env python3
"""
Test Configuration and Utilities
This file contains configuration settings and utility functions for test automation.
"""

import os
from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass
class TestConfig:
    """Configuration settings for test execution"""
    
    # Environment settings
    environment: str = "development"
    base_url: str = "http://localhost:8000"
    api_version: str = "v1"
    
    # Test execution settings
    timeout: int = 30
    retry_count: int = 3
    parallel_execution: bool = False
    max_workers: int = 4
    
    # Reporting settings
    report_format: str = "json"  # json, html, xml
    report_path: str = "./test_reports"
    log_level: str = "INFO"
    
    # Database settings (if needed)
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "test_db"
    db_user: str = "test_user"
    db_password: str = ""
    
    # Browser settings (for UI tests)
    browser: str = "chrome"  # chrome, firefox, safari
    headless: bool = True
    window_size: str = "1920x1080"
    
    @classmethod
    def from_env(cls) -> 'TestConfig':
        """Create configuration from environment variables"""
        return cls(
            environment=os.getenv("TEST_ENV", "development"),
            base_url=os.getenv("BASE_URL", "http://localhost:8000"),
            timeout=int(os.getenv("TEST_TIMEOUT", "30")),
            retry_count=int(os.getenv("RETRY_COUNT", "3")),
            report_path=os.getenv("REPORT_PATH", "./test_reports"),
            log_level=os.getenv("LOG_LEVEL", "INFO")
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary"""
        return {
            "environment": self.environment,
            "base_url": self.base_url,
            "api_version": self.api_version,
            "timeout": self.timeout,
            "retry_count": self.retry_count,
            "parallel_execution": self.parallel_execution,
            "max_workers": self.max_workers,
            "report_format": self.report_format,
            "report_path": self.report_path,
            "log_level": self.log_level,
            "browser": self.browser,
            "headless": self.headless,
            "window_size": self.window_size
        }


class TestDataGenerator:
    """Utility class for generating test data"""
    
    @staticmethod
    def generate_user_data(count: int = 1) -> list:
        """Generate sample user data"""
        users = []
        for i in range(1, count + 1):
            users.append({
                "id": i,
                "username": f"user{i}",
                "email": f"user{i}@example.com",
                "first_name": f"First{i}",
                "last_name": f"Last{i}",
                "is_active": True
            })
        return users
    
    @staticmethod
    def generate_api_response(status: str = "success", data: Any = None, 
                            error: Optional[str] = None) -> Dict:
        """Generate sample API response"""
        return {
            "status": status,
            "data": data,
            "error": error,
            "timestamp": "2025-01-01T00:00:00Z"
        }


class TestAssertion:
    """Custom assertion utilities"""
    
    @staticmethod
    def assert_dict_contains(actual: Dict, expected: Dict):
        """Assert that actual dictionary contains all expected key-value pairs"""
        for key, value in expected.items():
            assert key in actual, f"Key '{key}' not found in actual dictionary"
            assert actual[key] == value, \
                f"Value mismatch for key '{key}': expected {value}, got {actual[key]}"
    
    @staticmethod
    def assert_list_length(actual: list, expected_length: int):
        """Assert list has expected length"""
        assert len(actual) == expected_length, \
            f"List length mismatch: expected {expected_length}, got {len(actual)}"
    
    @staticmethod
    def assert_response_status(response: Dict, expected_status: str = "success"):
        """Assert API response has expected status"""
        assert "status" in response, "Response missing 'status' field"
        assert response["status"] == expected_status, \
            f"Status mismatch: expected {expected_status}, got {response['status']}"


class TestHelper:
    """Helper utilities for test execution"""
    
    @staticmethod
    def wait_for_condition(condition_func, timeout: int = 10, 
                          interval: float = 0.5) -> bool:
        """Wait for a condition to become true"""
        import time
        elapsed = 0
        while elapsed < timeout:
            if condition_func():
                return True
            time.sleep(interval)
            elapsed += interval
        return False
    
    @staticmethod
    def cleanup_test_files(directory: str, pattern: str = "*test*"):
        """Clean up test files matching pattern"""
        import glob
        files = glob.glob(os.path.join(directory, pattern))
        for file in files:
            try:
                os.remove(file)
            except Exception as e:
                print(f"Failed to remove {file}: {e}")
    
    @staticmethod
    def setup_test_directory(path: str) -> str:
        """Create test directory if it doesn't exist"""
        os.makedirs(path, exist_ok=True)
        return path


# Global test configuration instance
test_config = TestConfig.from_env()


if __name__ == "__main__":
    # Example usage
    print("Test Configuration:")
    print("-" * 50)
    config = TestConfig.from_env()
    for key, value in config.to_dict().items():
        print(f"{key}: {value}")
    
    print("\nSample User Data:")
    print("-" * 50)
    users = TestDataGenerator.generate_user_data(3)
    for user in users:
        print(user)
    
    print("\nSample API Response:")
    print("-" * 50)
    response = TestDataGenerator.generate_api_response(
        status="success",
        data={"message": "Operation completed successfully"}
    )
    print(response)

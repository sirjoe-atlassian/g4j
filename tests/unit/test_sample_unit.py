"""
Sample unit tests for test automation framework.
"""
import pytest
from src.config.config import Config


class TestConfiguration:
    """Test configuration functionality."""
    
    def test_config_has_api_base_url(self):
        """Test that configuration has API base URL."""
        assert hasattr(Config, 'API_BASE_URL')
        assert isinstance(Config.API_BASE_URL, str)
    
    def test_config_has_timeout(self):
        """Test that configuration has timeout setting."""
        assert hasattr(Config, 'API_TIMEOUT')
        assert isinstance(Config.API_TIMEOUT, int)
        assert Config.API_TIMEOUT > 0
    
    def test_get_config_returns_dict(self):
        """Test that get_config returns dictionary."""
        config_dict = Config.get_config()
        assert isinstance(config_dict, dict)
        assert 'api_base_url' in config_dict
        assert 'api_timeout' in config_dict


@pytest.mark.unit
class TestMathOperations:
    """Sample unit tests for basic operations."""
    
    def test_addition(self):
        """Test basic addition."""
        assert 2 + 2 == 4
    
    def test_subtraction(self):
        """Test basic subtraction."""
        assert 5 - 3 == 2
    
    def test_multiplication(self):
        """Test basic multiplication."""
        assert 3 * 4 == 12
    
    def test_division(self):
        """Test basic division."""
        assert 10 / 2 == 5
    
    def test_division_by_zero_raises_error(self):
        """Test that division by zero raises error."""
        with pytest.raises(ZeroDivisionError):
            result = 10 / 0

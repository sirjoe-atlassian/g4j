"""
Sample test cases demonstrating test automation capabilities.
"""

import pytest


class TestBasicFunctionality:
    """Test suite for basic functionality."""
    
    def test_simple_assertion(self):
        """Test simple assertion."""
        assert True, "This should always pass"
    
    def test_equality(self):
        """Test equality comparison."""
        expected = "g4j"
        actual = "g4j"
        assert expected == actual, f"Expected {expected}, got {actual}"
    
    def test_list_operations(self):
        """Test list operations."""
        test_list = [1, 2, 3, 4, 5]
        assert len(test_list) == 5, "List should have 5 elements"
        assert 3 in test_list, "3 should be in the list"
        assert test_list[0] == 1, "First element should be 1"


class TestWithFixtures:
    """Test suite demonstrating fixture usage."""
    
    def test_with_config(self, test_config):
        """Test using the test_config fixture."""
        assert test_config["project_name"] == "g4j"
        assert "environment" in test_config
        assert test_config["timeout"] > 0
    
    def test_with_mock_data(self, mock_data):
        """Test using mock data fixture."""
        assert "user" in mock_data
        assert mock_data["user"]["name"] == "Test User"
        assert len(mock_data["items"]) == 3
    
    def test_with_setup_teardown(self, setup_teardown):
        """Test using setup and teardown fixture."""
        # Test logic here
        result = 2 + 2
        assert result == 4, "Basic math should work"


class TestParameterized:
    """Test suite demonstrating parameterized tests."""
    
    @pytest.mark.parametrize("input_value,expected", [
        (1, 2),
        (2, 4),
        (3, 6),
        (4, 8),
        (5, 10),
    ])
    def test_multiply_by_two(self, input_value, expected):
        """Test multiplication by two with various inputs."""
        result = input_value * 2
        assert result == expected, f"Expected {expected}, got {result}"
    
    @pytest.mark.parametrize("text", [
        "hello",
        "world",
        "test",
        "automation",
    ])
    def test_string_length(self, text):
        """Test that strings have positive length."""
        assert len(text) > 0, "String should have positive length"


class TestExceptions:
    """Test suite for exception handling."""
    
    def test_exception_raised(self):
        """Test that an exception is raised."""
        with pytest.raises(ValueError):
            raise ValueError("This is expected")
    
    def test_zero_division(self):
        """Test zero division exception."""
        with pytest.raises(ZeroDivisionError):
            result = 1 / 0
    
    def test_type_error(self):
        """Test type error exception."""
        with pytest.raises(TypeError):
            result = "string" + 5


@pytest.mark.smoke
class TestSmokeTests:
    """Smoke tests for critical functionality."""
    
    def test_critical_path(self):
        """Test critical application path."""
        assert True, "Critical path test"
    
    def test_system_health(self, test_config):
        """Test system health check."""
        assert test_config is not None
        assert test_config["project_name"] == "g4j"


@pytest.mark.integration
class TestIntegration:
    """Integration tests."""
    
    def test_component_integration(self, mock_data):
        """Test integration between components."""
        user = mock_data["user"]
        items = mock_data["items"]
        
        # Simulate integration scenario
        assert user["id"] > 0
        assert len(items) > 0
        
        # Verify data consistency
        for item in items:
            assert "id" in item
            assert "name" in item
            assert "value" in item

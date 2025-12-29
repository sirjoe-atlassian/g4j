#!/usr/bin/env python3
"""
Pytest-based Test Suite for g4j Project
This file contains sample tests using the pytest framework.
"""

import pytest
import json
from typing import List, Dict


# Fixtures
@pytest.fixture
def sample_data():
    """Fixture providing sample test data"""
    return {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"},
            {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
        ]
    }


@pytest.fixture
def config():
    """Fixture providing test configuration"""
    return {
        "api_url": "https://api.example.com",
        "timeout": 30,
        "retry_count": 3
    }


# Unit Tests
class TestBasicOperations:
    """Test basic mathematical and string operations"""
    
    def test_addition(self):
        """Test addition operation"""
        assert 2 + 2 == 4
        assert 10 + 5 == 15
    
    def test_subtraction(self):
        """Test subtraction operation"""
        assert 10 - 5 == 5
        assert 100 - 50 == 50
    
    def test_multiplication(self):
        """Test multiplication operation"""
        assert 3 * 4 == 12
        assert 7 * 8 == 56
    
    def test_division(self):
        """Test division operation"""
        assert 10 / 2 == 5
        assert 100 / 4 == 25
    
    def test_string_concatenation(self):
        """Test string concatenation"""
        assert "Hello" + " " + "World" == "Hello World"
    
    def test_string_methods(self):
        """Test various string methods"""
        test_string = "python testing"
        assert test_string.upper() == "PYTHON TESTING"
        assert test_string.title() == "Python Testing"
        assert test_string.replace("python", "automated") == "automated testing"


class TestDataStructures:
    """Test data structure operations"""
    
    def test_list_operations(self):
        """Test list operations"""
        test_list = [1, 2, 3, 4, 5]
        assert len(test_list) == 5
        assert sum(test_list) == 15
        assert max(test_list) == 5
        assert min(test_list) == 1
    
    def test_dict_operations(self):
        """Test dictionary operations"""
        test_dict = {"a": 1, "b": 2, "c": 3}
        assert test_dict["a"] == 1
        assert "b" in test_dict
        assert len(test_dict.keys()) == 3
    
    def test_set_operations(self):
        """Test set operations"""
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        assert set1.union(set2) == {1, 2, 3, 4, 5, 6}
        assert set1.intersection(set2) == {3, 4}


class TestWithFixtures:
    """Test cases using pytest fixtures"""
    
    def test_sample_data_structure(self, sample_data):
        """Test that sample data has correct structure"""
        assert "users" in sample_data
        assert isinstance(sample_data["users"], list)
        assert len(sample_data["users"]) == 3
    
    def test_user_data_fields(self, sample_data):
        """Test that user data has required fields"""
        for user in sample_data["users"]:
            assert "id" in user
            assert "name" in user
            assert "email" in user
    
    def test_config_values(self, config):
        """Test configuration values"""
        assert config["timeout"] == 30
        assert config["retry_count"] == 3
        assert "api_url" in config


# Parametrized Tests
class TestParametrized:
    """Test cases with parametrized inputs"""
    
    @pytest.mark.parametrize("input,expected", [
        (2, 4),
        (3, 9),
        (4, 16),
        (5, 25),
        (10, 100)
    ])
    def test_square(self, input, expected):
        """Test squaring numbers"""
        assert input ** 2 == expected
    
    @pytest.mark.parametrize("text,expected", [
        ("hello", "HELLO"),
        ("world", "WORLD"),
        ("Python", "PYTHON"),
        ("test", "TEST")
    ])
    def test_uppercase(self, text, expected):
        """Test string uppercase conversion"""
        assert text.upper() == expected
    
    @pytest.mark.parametrize("value,is_positive", [
        (5, True),
        (-3, False),
        (0, False),
        (100, True),
        (-1, False)
    ])
    def test_positive_numbers(self, value, is_positive):
        """Test positive number detection"""
        assert (value > 0) == is_positive


# Exception Testing
class TestExceptions:
    """Test exception handling"""
    
    def test_zero_division(self):
        """Test zero division raises error"""
        with pytest.raises(ZeroDivisionError):
            1 / 0
    
    def test_key_error(self):
        """Test dictionary key error"""
        test_dict = {"a": 1}
        with pytest.raises(KeyError):
            _ = test_dict["b"]
    
    def test_type_error(self):
        """Test type error"""
        with pytest.raises(TypeError):
            "string" + 123


# Markers for test organization
@pytest.mark.smoke
class TestSmokeSuite:
    """Critical smoke tests"""
    
    def test_critical_path(self):
        """Test critical application path"""
        assert True
    
    def test_basic_functionality(self):
        """Test basic functionality"""
        assert 1 + 1 == 2


@pytest.mark.integration
class TestIntegration:
    """Integration tests"""
    
    def test_json_serialization(self, sample_data):
        """Test JSON serialization/deserialization"""
        json_string = json.dumps(sample_data)
        deserialized = json.loads(json_string)
        assert deserialized == sample_data
    
    def test_data_transformation(self, sample_data):
        """Test data transformation pipeline"""
        users = sample_data["users"]
        names = [user["name"] for user in users]
        assert len(names) == 3
        assert "Alice" in names


@pytest.mark.slow
class TestSlowOperations:
    """Tests that may take longer to execute"""
    
    def test_large_list_processing(self):
        """Test processing of large list"""
        large_list = list(range(10000))
        assert len(large_list) == 10000
        assert sum(large_list) == 49995000


# Skip and xfail examples
class TestConditional:
    """Tests with conditional execution"""
    
    @pytest.mark.skip(reason="Not implemented yet")
    def test_future_feature(self):
        """Test for future feature"""
        pass
    
    @pytest.mark.xfail(reason="Known bug")
    def test_known_issue(self):
        """Test with known issue"""
        assert False


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

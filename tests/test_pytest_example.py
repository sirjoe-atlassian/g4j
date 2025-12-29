"""
Pytest-based test automation examples for g4j project.
Demonstrates pytest-style testing with fixtures and parametrization.
"""

import pytest


def test_basic_assertions():
    """Test basic assertions with pytest."""
    assert True
    assert not False
    assert 1 + 1 == 2
    assert "hello".upper() == "HELLO"


def test_with_sample_data(sample_data):
    """Test using the sample_data fixture."""
    assert "name" in sample_data
    assert sample_data["name"] == "Test User"
    assert sample_data["email"] == "test@example.com"
    assert sample_data["age"] == 30
    assert sample_data["active"] is True


def test_with_sample_list(sample_list):
    """Test using the sample_list fixture."""
    assert len(sample_list) == 10
    assert sample_list[0] == 1
    assert sample_list[-1] == 10
    assert sum(sample_list) == 55


def test_with_mock_api_response(mock_api_response):
    """Test using mock API response fixture."""
    assert mock_api_response["status"] == 200
    assert "data" in mock_api_response
    assert mock_api_response["data"]["id"] == 1
    assert mock_api_response["message"] == "Success"


@pytest.mark.parametrize("input_value,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
    (4, 8),
    (5, 10),
])
def test_parametrized_multiply(input_value, expected):
    """Test parametrized multiplication."""
    assert input_value * 2 == expected


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (10, 20, 30),
    (100, 200, 300),
])
def test_parametrized_addition(a, b, expected):
    """Test parametrized addition."""
    assert a + b == expected


def test_string_operations():
    """Test various string operations."""
    test_string = "Hello, World!"
    
    assert "World" in test_string
    assert test_string.startswith("Hello")
    assert test_string.endswith("!")
    assert len(test_string) == 13


def test_list_operations():
    """Test various list operations."""
    test_list = [1, 2, 3, 4, 5]
    
    assert len(test_list) == 5
    assert 3 in test_list
    assert test_list[0] == 1
    assert test_list[-1] == 5
    
    test_list.append(6)
    assert len(test_list) == 6
    assert test_list[-1] == 6


def test_dictionary_operations():
    """Test various dictionary operations."""
    test_dict = {"a": 1, "b": 2, "c": 3}
    
    assert len(test_dict) == 3
    assert "a" in test_dict
    assert test_dict["a"] == 1
    assert list(test_dict.keys()) == ["a", "b", "c"]
    assert list(test_dict.values()) == [1, 2, 3]


def test_exception_handling():
    """Test exception handling with pytest."""
    with pytest.raises(ZeroDivisionError):
        _ = 1 / 0
    
    with pytest.raises(KeyError):
        test_dict = {"key": "value"}
        _ = test_dict["nonexistent"]
    
    with pytest.raises(ValueError):
        int("not a number")


class TestClassExample:
    """Example test class using pytest class-based testing."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup method that runs before each test."""
        self.test_value = 42
        yield
        # Teardown code here if needed
        self.test_value = None
    
    def test_class_method_one(self):
        """First test method in class."""
        assert self.test_value == 42
    
    def test_class_method_two(self):
        """Second test method in class."""
        assert self.test_value * 2 == 84
    
    def test_class_method_three(self, sample_data):
        """Test method using external fixture."""
        assert self.test_value == 42
        assert sample_data["age"] == 30


@pytest.mark.slow
def test_marked_as_slow():
    """Test marked as slow (can be skipped with -m 'not slow')."""
    assert True


@pytest.mark.skip(reason="Demonstrating skip functionality")
def test_skip_example():
    """This test will be skipped."""
    assert False


@pytest.mark.skipif(True, reason="Conditional skip example")
def test_conditional_skip():
    """This test will be conditionally skipped."""
    assert False

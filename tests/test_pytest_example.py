"""
Pytest-based test automation examples.
This module demonstrates pytest test structure with fixtures.
"""

import pytest


def test_basic_assertion():
    """Test basic assertion."""
    assert 1 + 1 == 2


def test_with_sample_data(sample_data):
    """Test using sample_data fixture."""
    assert sample_data['name'] == 'g4j'
    assert 'version' in sample_data
    assert sample_data['description'] is not None


def test_with_sample_list(sample_list):
    """Test using sample_list fixture."""
    assert len(sample_list) == 5
    assert 3 in sample_list
    assert sample_list[0] == 1


def test_with_config(test_config):
    """Test using test_config fixture."""
    assert test_config['environment'] == 'test'
    assert test_config['debug'] is True


@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
    (4, 8),
])
def test_multiply_by_two(input, expected):
    """Test parameterized test case."""
    assert input * 2 == expected


class TestClass:
    """Example test class using pytest."""
    
    def test_method_one(self):
        """First test method."""
        assert "hello".upper() == "HELLO"
    
    def test_method_two(self):
        """Second test method."""
        assert [1, 2, 3] == [1, 2, 3]

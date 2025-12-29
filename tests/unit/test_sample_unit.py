"""Sample unit tests."""
import pytest


class Calculator:
    """Simple calculator for testing."""
    
    @staticmethod
    def add(a, b):
        """Add two numbers."""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Subtract two numbers."""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers."""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


@pytest.fixture
def calculator():
    """Provide calculator instance."""
    return Calculator()


@pytest.mark.unit
@pytest.mark.smoke
class TestCalculator:
    """Test calculator functionality."""
    
    def test_addition(self, calculator):
        """Test addition operation."""
        result = calculator.add(5, 3)
        assert result == 8, "Addition failed"
    
    def test_subtraction(self, calculator):
        """Test subtraction operation."""
        result = calculator.subtract(10, 4)
        assert result == 6, "Subtraction failed"
    
    def test_multiplication(self, calculator):
        """Test multiplication operation."""
        result = calculator.multiply(4, 5)
        assert result == 20, "Multiplication failed"
    
    def test_division(self, calculator):
        """Test division operation."""
        result = calculator.divide(20, 4)
        assert result == 5, "Division failed"
    
    def test_division_by_zero(self, calculator):
        """Test division by zero raises error."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculator.divide(10, 0)
    
    @pytest.mark.parametrize("a,b,expected", [
        (0, 0, 0),
        (1, 1, 2),
        (-1, 1, 0),
        (-1, -1, -2),
        (100, 200, 300),
    ])
    def test_addition_parametrized(self, calculator, a, b, expected):
        """Test addition with multiple inputs."""
        result = calculator.add(a, b)
        assert result == expected

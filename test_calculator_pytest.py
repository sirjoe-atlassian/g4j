import pytest
from example_calculator import Calculator


class TestCalculator:
    """Test suite for Calculator."""
    
    @pytest.fixture
    def instance(self):
        """Create a Calculator instance for testing."""
        return Calculator()
    
    def test_add(self, instance):
        """Test the add method."""
        result = instance.add(2, 3)
        assert result == 5, "2 + 3 should equal 5"
        assert "2 + 3 = 5" in instance.get_history()
    
    def test_subtract(self, instance):
        """Test the subtract method."""
        result = instance.subtract(10, 4)
        assert result == 6, "10 - 4 should equal 6"
        assert "10 - 4 = 6" in instance.get_history()
    
    def test_multiply(self, instance):
        """Test the multiply method."""
        result = instance.multiply(3, 7)
        assert result == 21, "3 * 7 should equal 21"
        assert "3 * 7 = 21" in instance.get_history()
    
    def test_divide(self, instance):
        """Test the divide method."""
        result = instance.divide(20, 4)
        assert result == 5, "20 / 4 should equal 5"
        assert "20 / 4 = 5.0" in instance.get_history()
    
    def test_divide_by_zero(self, instance):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            instance.divide(10, 0)
    
    def test_calculator_initialization(self, instance):
        """Test that Calculator initializes correctly."""
        assert instance is not None
        assert isinstance(instance, Calculator)
        assert instance.get_history() == []
    
    def test_history_tracking(self, instance):
        """Test that calculation history is tracked correctly."""
        instance.add(1, 1)
        instance.subtract(5, 2)
        history = instance.get_history()
        assert len(history) == 2
        assert "1 + 1 = 2" in history
        assert "5 - 2 = 3" in history
    
    def test_clear_history(self, instance):
        """Test that history can be cleared."""
        instance.add(1, 1)
        instance.multiply(2, 3)
        assert len(instance.get_history()) == 2
        instance.clear_history()
        assert instance.get_history() == []

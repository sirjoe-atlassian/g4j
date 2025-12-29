import unittest
from example_calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test suite for Calculator."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.instance = Calculator()
    
    def tearDown(self):
        """Clean up after tests."""
        self.instance = None
    
    def test_add(self):
        """Test the add method."""
        result = self.instance.add(2, 3)
        self.assertEqual(result, 5, "2 + 3 should equal 5")
        self.assertIn("2 + 3 = 5", self.instance.get_history())
    
    def test_subtract(self):
        """Test the subtract method."""
        result = self.instance.subtract(10, 4)
        self.assertEqual(result, 6, "10 - 4 should equal 6")
        self.assertIn("10 - 4 = 6", self.instance.get_history())
    
    def test_multiply(self):
        """Test the multiply method."""
        result = self.instance.multiply(3, 7)
        self.assertEqual(result, 21, "3 * 7 should equal 21")
        self.assertIn("3 * 7 = 21", self.instance.get_history())
    
    def test_divide(self):
        """Test the divide method."""
        result = self.instance.divide(20, 4)
        self.assertEqual(result, 5, "20 / 4 should equal 5")
        self.assertIn("20 / 4 = 5.0", self.instance.get_history())
    
    def test_divide_by_zero(self):
        """Test that dividing by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.instance.divide(10, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))
    
    def test_calculator_initialization(self):
        """Test that Calculator initializes correctly."""
        self.assertIsNotNone(self.instance)
        self.assertIsInstance(self.instance, Calculator)
        self.assertEqual(self.instance.get_history(), [])
    
    def test_history_tracking(self):
        """Test that calculation history is tracked correctly."""
        self.instance.add(1, 1)
        self.instance.subtract(5, 2)
        history = self.instance.get_history()
        self.assertEqual(len(history), 2)
        self.assertIn("1 + 1 = 2", history)
        self.assertIn("5 - 2 = 3", history)
    
    def test_clear_history(self):
        """Test that history can be cleared."""
        self.instance.add(1, 1)
        self.instance.multiply(2, 3)
        self.assertEqual(len(self.instance.get_history()), 2)
        self.instance.clear_history()
        self.assertEqual(self.instance.get_history(), [])


if __name__ == '__main__':
    unittest.main()

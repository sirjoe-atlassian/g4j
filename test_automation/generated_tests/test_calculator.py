"""
Calculator Test Suite
Auto-generated on 2025-12-29 05:08:05
"""

import unittest

class TestCalculator(unittest.TestCase):
    """Test cases for Calculator"""
    
    def test_addition(self):
        """Test addition of two numbers"""
        # Arrange
        calc = Calculator()
        
        # Act
        result = calc.add(2, 3)
        
        # Assert
        self.assertEqual(result, 5)

class TestCalculator(unittest.TestCase):
    """Test cases for Calculator"""
    
    def test_subtraction(self):
        """Test subtraction of two numbers"""
        # Arrange
        calc = Calculator()
        
        # Act
        result = calc.subtract(5, 3)
        
        # Assert
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()

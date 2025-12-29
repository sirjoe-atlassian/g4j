"""
Example Calculator class for demonstrating test generation.
"""


class Calculator:
    """A simple calculator class."""
    
    def __init__(self):
        """Initialize the calculator."""
        self.history = []
    
    def add(self, a: float, b: float) -> float:
        """
        Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """
        Subtract b from a.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Difference of a and b
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """
        Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """
        Divide a by b.
        
        Args:
            a: First number (numerator)
            b: Second number (denominator)
            
        Returns:
            Quotient of a and b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def clear_history(self):
        """Clear the calculation history."""
        self.history = []
    
    def get_history(self) -> list:
        """
        Get the calculation history.
        
        Returns:
            List of calculation strings
        """
        return self.history.copy()

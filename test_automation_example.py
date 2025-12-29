"""
Example usage of the Test Automation Framework
This demonstrates how to use the test automation framework in your own projects.
"""

from test_automation import TestAutomation


def main():
    """Main function to demonstrate test automation usage."""
    
    # Create a new test automation instance
    automation = TestAutomation()
    
    # Example: Testing a simple calculator
    class Calculator:
        @staticmethod
        def add(a, b):
            return a + b
        
        @staticmethod
        def subtract(a, b):
            return a - b
        
        @staticmethod
        def multiply(a, b):
            return a * b
        
        @staticmethod
        def divide(a, b):
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b
    
    calc = Calculator()
    
    # Define test cases
    def test_addition():
        """Test calculator addition."""
        assert calc.add(2, 3) == 5
        assert calc.add(-1, 1) == 0
        assert calc.add(0, 0) == 0
    
    def test_subtraction():
        """Test calculator subtraction."""
        assert calc.subtract(5, 3) == 2
        assert calc.subtract(0, 5) == -5
        assert calc.subtract(10, 10) == 0
    
    def test_multiplication():
        """Test calculator multiplication."""
        assert calc.multiply(2, 3) == 6
        assert calc.multiply(0, 100) == 0
        assert calc.multiply(-2, 3) == -6
    
    def test_division():
        """Test calculator division."""
        assert calc.divide(6, 2) == 3
        assert calc.divide(10, 5) == 2
        assert calc.divide(7, 2) == 3.5
    
    def test_division_by_zero():
        """Test division by zero raises error."""
        try:
            calc.divide(5, 0)
            assert False, "Should have raised ValueError"
        except ValueError as e:
            assert str(e) == "Cannot divide by zero"
    
    # Register all tests
    automation.register_test("Addition Tests", test_addition)
    automation.register_test("Subtraction Tests", test_subtraction)
    automation.register_test("Multiplication Tests", test_multiplication)
    automation.register_test("Division Tests", test_division)
    automation.register_test("Division by Zero Test", test_division_by_zero)
    
    # Run all tests
    results = automation.run_all_tests()
    
    # Check if all tests passed
    all_passed = all(r.passed for r in results)
    
    if all_passed:
        print("✓ All tests passed successfully!")
        return 0
    else:
        print("✗ Some tests failed. Please review the results above.")
        return 1


if __name__ == "__main__":
    exit(main())

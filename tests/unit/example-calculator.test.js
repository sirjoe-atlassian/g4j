/**
 * Example unit test demonstrating the test framework
 */

class Calculator {
  add(a, b) {
    return a + b;
  }

  subtract(a, b) {
    return a - b;
  }

  multiply(a, b) {
    return a * b;
  }

  divide(a, b) {
    if (b === 0) {
      throw new Error('Division by zero');
    }
    return a / b;
  }
}

describe('Calculator', () => {
  let calculator;

  beforeEach(() => {
    calculator = new Calculator();
  });

  test('should add two numbers correctly', () => {
    // Arrange
    const a = 5;
    const b = 3;
    
    // Act
    const result = calculator.add(a, b);
    
    // Assert
    expect(result).toBe(8);
  });

  test('should subtract two numbers correctly', () => {
    // Arrange
    const a = 10;
    const b = 4;
    
    // Act
    const result = calculator.subtract(a, b);
    
    // Assert
    expect(result).toBe(6);
  });

  test('should multiply two numbers correctly', () => {
    // Arrange
    const a = 6;
    const b = 7;
    
    // Act
    const result = calculator.multiply(a, b);
    
    // Assert
    expect(result).toBe(42);
  });

  test('should divide two numbers correctly', () => {
    // Arrange
    const a = 15;
    const b = 3;
    
    // Act
    const result = calculator.divide(a, b);
    
    // Assert
    expect(result).toBe(5);
  });

  test('should throw error when dividing by zero', () => {
    // Arrange
    const a = 10;
    const b = 0;
    
    // Act & Assert
    expect(() => calculator.divide(a, b)).toThrow('Division by zero');
  });
});

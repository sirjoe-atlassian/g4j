#!/usr/bin/env python3
"""
Unit tests for test automation generator
"""

import pytest
from test_automation_generator import TestGenerator, TestFramework, Language


class TestTestGenerator:
    """Test the TestGenerator class"""
    
    def test_pytest_generation(self):
        """Test pytest test generation"""
        generator = TestGenerator(TestFramework.PYTEST, Language.PYTHON)
        code = generator.generate_test_class("Calculator", ["add", "subtract"])
        
        assert "import pytest" in code
        assert "class TestCalculator:" in code
        assert "def test_add(self):" in code
        assert "def test_subtract(self):" in code
        assert "assert True" in code
    
    def test_unittest_generation(self):
        """Test unittest test generation"""
        generator = TestGenerator(TestFramework.UNITTEST, Language.PYTHON)
        code = generator.generate_test_class("Calculator", ["add", "subtract"])
        
        assert "import unittest" in code
        assert "class TestCalculator(unittest.TestCase):" in code
        assert "def setUp(self):" in code
        assert "def tearDown(self):" in code
        assert "def test_add(self):" in code
        assert "def test_subtract(self):" in code
        assert "self.assertTrue" in code
    
    def test_jest_generation(self):
        """Test Jest test generation for JavaScript"""
        generator = TestGenerator(TestFramework.JEST, Language.JAVASCRIPT)
        code = generator.generate_test_class("Calculator", ["add", "subtract"])
        
        assert "describe('Calculator'" in code
        assert "test('should add'" in code
        assert "test('should subtract'" in code
        assert "expect(true).toBe(true)" in code
    
    def test_jest_typescript_generation(self):
        """Test Jest test generation for TypeScript"""
        generator = TestGenerator(TestFramework.JEST, Language.TYPESCRIPT)
        code = generator.generate_test_class("Calculator", ["add", "subtract"])
        
        assert "describe('Calculator'" in code
        assert "test('should add'" in code
        assert "(): void =>" in code
        assert "expect(true).toBe(true)" in code
    
    def test_mocha_generation(self):
        """Test Mocha test generation"""
        generator = TestGenerator(TestFramework.MOCHA, Language.JAVASCRIPT)
        code = generator.generate_test_class("Calculator", ["add", "subtract"])
        
        assert "const { expect } = require('chai')" in code
        assert "describe('Calculator'" in code
        assert "it('should add'" in code
        assert "it('should subtract'" in code
        assert "expect(true).to.be.true" in code
    
    def test_junit_generation(self):
        """Test JUnit test generation"""
        generator = TestGenerator(TestFramework.JUNIT, Language.JAVA)
        code = generator.generate_test_class("Calculator", ["add", "subtract"])
        
        assert "import org.junit.jupiter.api.Test" in code
        assert "public class CalculatorTest" in code
        assert "@BeforeEach" in code
        assert "@AfterEach" in code
        assert "@Test" in code
        assert "public void testAdd()" in code
        assert "public void testSubtract()" in code
        assert "assertTrue" in code
    
    def test_generate_test_suite(self):
        """Test generating multiple test files"""
        generator = TestGenerator(TestFramework.PYTEST, Language.PYTHON)
        
        specs = [
            {"class_name": "Calculator", "methods": ["add", "subtract"]},
            {"class_name": "StringUtils", "methods": ["concat", "split"]}
        ]
        
        test_files = generator.generate_test_suite(specs)
        
        assert "test_calculator.py" in test_files
        assert "test_stringutils.py" in test_files
        assert "def test_add(self):" in test_files["test_calculator.py"]
        assert "def test_concat(self):" in test_files["test_stringutils.py"]
    
    def test_unsupported_language_raises_error(self):
        """Test that unsupported language raises ValueError"""
        generator = TestGenerator(TestFramework.PYTEST, Language.PYTHON)
        generator.language = "unsupported"
        
        with pytest.raises(ValueError, match="Unsupported language"):
            generator.generate_test_class("Test", ["method"])
    
    def test_unsupported_framework_raises_error(self):
        """Test that unsupported framework raises ValueError"""
        generator = TestGenerator(TestFramework.PYTEST, Language.PYTHON)
        generator.framework = "unsupported"
        
        with pytest.raises(ValueError, match="Unsupported framework"):
            generator.generate_test_class("Test", ["method"])

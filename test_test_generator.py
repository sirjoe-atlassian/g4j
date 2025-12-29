#!/usr/bin/env python3
"""
Unit tests for the test generator module
"""

import pytest
import json
import os
from test_generator import (
    TestCase,
    TestFramework,
    Language,
    TestGenerator,
    PytestGenerator,
    UnittestGenerator,
    JUnitGenerator,
    JestGenerator,
    create_generator,
    generate_from_json
)


class TestTestCase:
    """Tests for TestCase dataclass"""
    
    def test_test_case_creation(self):
        """Test creating a basic test case"""
        tc = TestCase(
            name="example",
            description="Example test"
        )
        assert tc.name == "example"
        assert tc.description == "Example test"
        assert tc.assertions == []
        assert tc.test_data == {}
    
    def test_test_case_with_assertions(self):
        """Test creating a test case with assertions"""
        assertions = ["assert x == 5", "assert y == 10"]
        tc = TestCase(
            name="with_assertions",
            description="Test with assertions",
            assertions=assertions
        )
        assert tc.assertions == assertions
    
    def test_test_case_with_setup_teardown(self):
        """Test creating a test case with setup and teardown"""
        tc = TestCase(
            name="full_test",
            description="Complete test",
            setup="setup_code()",
            teardown="cleanup()"
        )
        assert tc.setup == "setup_code()"
        assert tc.teardown == "cleanup()"


class TestPytestGenerator:
    """Tests for PytestGenerator"""
    
    def test_generator_initialization(self):
        """Test pytest generator initialization"""
        gen = PytestGenerator()
        assert gen.framework == TestFramework.PYTEST
        assert gen.language == Language.PYTHON
    
    def test_generate_single_test_case(self):
        """Test generating a single pytest test case"""
        gen = PytestGenerator()
        tc = TestCase(
            name="example",
            description="Example test",
            assertions=["assert True"]
        )
        code = gen.generate_test_case(tc)
        
        assert "def test_example" in code
        assert "Example test" in code
        assert "assert True" in code
    
    def test_generate_test_suite(self):
        """Test generating a complete pytest test suite"""
        gen = PytestGenerator()
        test_cases = [
            TestCase(
                name="test1",
                description="First test",
                assertions=["assert 1 == 1"]
            ),
            TestCase(
                name="test2",
                description="Second test",
                assertions=["assert 2 == 2"]
            )
        ]
        
        code = gen.generate_test_suite(test_cases, "MyTests")
        
        assert "import pytest" in code
        assert "class MyTests:" in code
        assert "def test_test1" in code
        assert "def test_test2" in code
    
    def test_generate_with_setup_teardown(self):
        """Test generating test with setup and teardown"""
        gen = PytestGenerator()
        tc = TestCase(
            name="complex",
            description="Complex test",
            setup="x = 5",
            teardown="del x",
            assertions=["assert x == 5"]
        )
        
        code = gen.generate_test_case(tc)
        
        assert "# Setup" in code
        assert "x = 5" in code
        assert "# Teardown" in code
        assert "del x" in code


class TestUnittestGenerator:
    """Tests for UnittestGenerator"""
    
    def test_generator_initialization(self):
        """Test unittest generator initialization"""
        gen = UnittestGenerator()
        assert gen.framework == TestFramework.UNITTEST
        assert gen.language == Language.PYTHON
    
    def test_generate_test_suite(self):
        """Test generating unittest test suite"""
        gen = UnittestGenerator()
        test_cases = [
            TestCase(
                name="example",
                description="Example test",
                assertions=["self.assertTrue(True)"]
            )
        ]
        
        code = gen.generate_test_suite(test_cases, "MyTests")
        
        assert "import unittest" in code
        assert "class MyTests(unittest.TestCase):" in code
        assert "def test_example" in code
        assert 'if __name__ == "__main__":' in code
        assert "unittest.main()" in code


class TestJUnitGenerator:
    """Tests for JUnitGenerator"""
    
    def test_generator_initialization(self):
        """Test JUnit generator initialization"""
        gen = JUnitGenerator()
        assert gen.framework == TestFramework.JUNIT
        assert gen.language == Language.JAVA
    
    def test_generate_test_case(self):
        """Test generating JUnit test case"""
        gen = JUnitGenerator()
        tc = TestCase(
            name="example",
            description="Example test",
            assertions=["assertTrue(true);"]
        )
        
        code = gen.generate_test_case(tc)
        
        assert "@Test" in code
        assert "public void testExample()" in code
        assert "assertTrue(true);" in code
    
    def test_generate_test_suite(self):
        """Test generating JUnit test suite"""
        gen = JUnitGenerator()
        test_cases = [
            TestCase(
                name="example",
                description="Example test",
                assertions=["assertEquals(5, result);"]
            )
        ]
        
        code = gen.generate_test_suite(test_cases, "MyTests")
        
        assert "import org.junit.jupiter.api.Test;" in code
        assert "public class MyTests {" in code
        assert "@Test" in code


class TestJestGenerator:
    """Tests for JestGenerator"""
    
    def test_generator_initialization(self):
        """Test Jest generator initialization"""
        gen = JestGenerator()
        assert gen.framework == TestFramework.JEST
        assert gen.language == Language.JAVASCRIPT
    
    def test_generate_test_case(self):
        """Test generating Jest test case"""
        gen = JestGenerator()
        tc = TestCase(
            name="example",
            description="Example test",
            assertions=["expect(result).toBe(5);"]
        )
        
        code = gen.generate_test_case(tc)
        
        assert "test('example'" in code
        assert "Example test" in code
        assert "expect(result).toBe(5);" in code
    
    def test_generate_test_suite(self):
        """Test generating Jest test suite"""
        gen = JestGenerator()
        test_cases = [
            TestCase(
                name="example",
                description="Example test",
                assertions=["expect(true).toBe(true);"]
            )
        ]
        
        code = gen.generate_test_suite(test_cases, "MyTests")
        
        assert "describe('MyTests'" in code
        assert "test('example'" in code


class TestGeneratorFactory:
    """Tests for create_generator factory function"""
    
    def test_create_pytest_generator(self):
        """Test creating pytest generator"""
        gen = create_generator(TestFramework.PYTEST)
        assert isinstance(gen, PytestGenerator)
    
    def test_create_unittest_generator(self):
        """Test creating unittest generator"""
        gen = create_generator(TestFramework.UNITTEST)
        assert isinstance(gen, UnittestGenerator)
    
    def test_create_junit_generator(self):
        """Test creating JUnit generator"""
        gen = create_generator(TestFramework.JUNIT)
        assert isinstance(gen, JUnitGenerator)
    
    def test_create_jest_generator(self):
        """Test creating Jest generator"""
        gen = create_generator(TestFramework.JEST)
        assert isinstance(gen, JestGenerator)
    
    def test_unsupported_framework(self):
        """Test that unsupported framework raises error"""
        # This would require adding MOCHA to the factory first
        # For now, we test with a mock enum value
        with pytest.raises(ValueError):
            create_generator(TestFramework.MOCHA)


class TestJSONGeneration:
    """Tests for JSON-based test generation"""
    
    def test_generate_from_json(self, tmp_path):
        """Test generating tests from JSON file"""
        # Create test JSON file
        json_file = tmp_path / "test_spec.json"
        spec = {
            "class_name": "GeneratedTests",
            "test_cases": [
                {
                    "name": "json_test",
                    "description": "Test from JSON",
                    "assertions": ["assert True"]
                }
            ]
        }
        
        with open(json_file, 'w') as f:
            json.dump(spec, f)
        
        # Generate test file
        output_file = tmp_path / "test_generated.py"
        generate_from_json(
            str(json_file),
            TestFramework.PYTEST,
            str(output_file)
        )
        
        # Verify output
        assert output_file.exists()
        content = output_file.read_text()
        assert "class GeneratedTests:" in content
        assert "def test_json_test" in content
        assert "Test from JSON" in content
    
    def test_generate_from_json_with_multiple_tests(self, tmp_path):
        """Test generating multiple tests from JSON"""
        json_file = tmp_path / "test_spec.json"
        spec = {
            "class_name": "MultipleTests",
            "test_cases": [
                {
                    "name": "test1",
                    "description": "First test",
                    "assertions": ["assert 1 == 1"]
                },
                {
                    "name": "test2",
                    "description": "Second test",
                    "setup": "x = 2",
                    "assertions": ["assert x == 2"]
                }
            ]
        }
        
        with open(json_file, 'w') as f:
            json.dump(spec, f)
        
        output_file = tmp_path / "test_multiple.py"
        generate_from_json(
            str(json_file),
            TestFramework.PYTEST,
            str(output_file)
        )
        
        content = output_file.read_text()
        assert "def test_test1" in content
        assert "def test_test2" in content
        assert "x = 2" in content


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

"""
Unit tests for the test generator module.
"""

import unittest
import json
import os
import tempfile
import shutil
from test_generator import TestGenerator


class TestTestGenerator(unittest.TestCase):
    """Test cases for TestGenerator class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.temp_dir = tempfile.mkdtemp()
        self.generator_pytest = TestGenerator(framework="pytest")
        self.generator_unittest = TestGenerator(framework="unittest")
        
        self.sample_test_cases = [
            {
                "name": "addition",
                "description": "Test addition",
                "inputs": {"a": 1, "b": 2},
                "expected": 3
            }
        ]
    
    def tearDown(self):
        """Clean up test fixtures"""
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    
    def test_init_pytest(self):
        """Test initialization with pytest framework"""
        generator = TestGenerator(framework="pytest")
        self.assertEqual(generator.framework, "pytest")
        self.assertEqual(generator.tests, [])
    
    def test_init_unittest(self):
        """Test initialization with unittest framework"""
        generator = TestGenerator(framework="unittest")
        self.assertEqual(generator.framework, "unittest")
    
    def test_generate_pytest_class(self):
        """Test generation of pytest test class"""
        code = self.generator_pytest.generate_test_class(
            "TestExample",
            self.sample_test_cases
        )
        
        self.assertIn("import pytest", code)
        self.assertIn("class TestExample:", code)
        self.assertIn("def test_addition(self):", code)
        self.assertIn("Test addition", code)
        self.assertIn("assert result == 3", code)
    
    def test_generate_unittest_class(self):
        """Test generation of unittest test class"""
        code = self.generator_unittest.generate_test_class(
            "TestExample",
            self.sample_test_cases
        )
        
        self.assertIn("import unittest", code)
        self.assertIn("class TestExample(unittest.TestCase):", code)
        self.assertIn("def test_addition(self):", code)
        self.assertIn("Test addition", code)
        self.assertIn("self.assertEqual(result, 3)", code)
        self.assertIn('if __name__ == "__main__":', code)
    
    def test_generate_from_json(self):
        """Test generation from JSON specification"""
        json_spec = json.dumps({
            "class_name": "TestFromJson",
            "test_cases": self.sample_test_cases
        })
        
        code = self.generator_pytest.generate_from_json(json_spec)
        
        self.assertIn("class TestFromJson:", code)
        self.assertIn("def test_addition(self):", code)
    
    def test_save_test_file(self):
        """Test saving generated test to file"""
        code = "# Test code"
        filename = "test_output.py"
        
        filepath = self.generator_pytest.save_test_file(
            code,
            filename,
            output_dir=self.temp_dir
        )
        
        self.assertTrue(os.path.exists(filepath))
        
        with open(filepath, 'r') as f:
            content = f.read()
        
        self.assertEqual(content, code)
    
    def test_unsupported_framework(self):
        """Test error handling for unsupported framework"""
        generator = TestGenerator(framework="unsupported")
        
        with self.assertRaises(ValueError) as context:
            generator.generate_test_class("TestFail", self.sample_test_cases)
        
        self.assertIn("Unsupported framework", str(context.exception))
    
    def test_multiple_test_cases(self):
        """Test generation with multiple test cases"""
        test_cases = [
            {
                "name": "test1",
                "description": "First test",
                "inputs": {"x": 1},
                "expected": 1
            },
            {
                "name": "test2",
                "description": "Second test",
                "inputs": {"y": 2},
                "expected": 2
            },
            {
                "name": "test3",
                "description": "Third test",
                "inputs": {"z": 3},
                "expected": 3
            }
        ]
        
        code = self.generator_pytest.generate_test_class("TestMultiple", test_cases)
        
        self.assertIn("def test_test1(self):", code)
        self.assertIn("def test_test2(self):", code)
        self.assertIn("def test_test3(self):", code)
    
    def test_test_case_without_expected(self):
        """Test generation when expected value is not provided"""
        test_cases = [
            {
                "name": "no_expected",
                "description": "Test without expected value",
                "inputs": {"x": 1}
            }
        ]
        
        code = self.generator_pytest.generate_test_class("TestNoExpected", test_cases)
        
        self.assertIn("assert result is not None", code)
    
    def test_output_directory_creation(self):
        """Test that output directory is created if it doesn't exist"""
        new_dir = os.path.join(self.temp_dir, "new_tests", "nested")
        
        filepath = self.generator_pytest.save_test_file(
            "# Test",
            "test.py",
            output_dir=new_dir
        )
        
        self.assertTrue(os.path.exists(new_dir))
        self.assertTrue(os.path.exists(filepath))


if __name__ == "__main__":
    unittest.main()

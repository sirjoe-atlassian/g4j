"""
Unit tests for test_automation_generator module
"""

import pytest
import os
import tempfile
from test_automation_generator import (
    TestCodeGenerator,
    TestConfig,
    TestFramework,
    TestType,
    generate_test_file
)


class TestTestCodeGenerator:
    """Test cases for TestCodeGenerator class"""
    
    def test_pytest_generation(self):
        """Test pytest code generation"""
        config = TestConfig(
            framework=TestFramework.PYTEST,
            test_type=TestType.UNIT,
            test_name="sample_test",
            module_path="mymodule",
            include_fixtures=True,
            include_mocks=True,
            include_parametrize=False
        )
        
        generator = TestCodeGenerator(config)
        code = generator.generate()
        
        assert "import pytest" in code
        assert "def test_sample_test" in code
        assert "@pytest.fixture" in code
        assert "from unittest.mock import" in code
    
    def test_unittest_generation(self):
        """Test unittest code generation"""
        config = TestConfig(
            framework=TestFramework.UNITTEST,
            test_type=TestType.UNIT,
            test_name="sample_test",
            module_path="mymodule",
            include_fixtures=True,
            include_mocks=True
        )
        
        generator = TestCodeGenerator(config)
        code = generator.generate()
        
        assert "import unittest" in code
        assert "class TestSample_Test(unittest.TestCase)" in code
        assert "def setUp(self)" in code
        assert "def tearDown(self)" in code
        assert "def test_sample_test(self)" in code
    
    def test_jest_generation(self):
        """Test Jest code generation"""
        config = TestConfig(
            framework=TestFramework.JEST,
            test_type=TestType.UNIT,
            test_name="sample_test",
            module_path="mymodule",
            include_fixtures=True,
            include_mocks=False
        )
        
        generator = TestCodeGenerator(config)
        code = generator.generate()
        
        assert "describe('sample_test'" in code
        assert "test('should sample_test'" in code
        assert "beforeEach" in code
        assert "expect(result).toBe(expected)" in code
    
    def test_junit_generation(self):
        """Test JUnit code generation"""
        config = TestConfig(
            framework=TestFramework.JUNIT,
            test_type=TestType.UNIT,
            test_name="sample_test",
            module_path="com.example",
            include_fixtures=True,
            include_mocks=True
        )
        
        generator = TestCodeGenerator(config)
        code = generator.generate()
        
        assert "import org.junit.jupiter.api.*" in code
        assert "public class TestSample_Test" in code
        assert "@BeforeEach" in code
        assert "@Test" in code
        assert "public void testSample_Test()" in code
    
    def test_api_test_generation_pytest(self):
        """Test API test generation for pytest"""
        config = TestConfig(
            framework=TestFramework.PYTEST,
            test_type=TestType.API,
            test_name="api_endpoint",
            module_path="api_module",
            include_mocks=True
        )
        
        generator = TestCodeGenerator(config)
        code = generator.generate()
        
        assert "def test_api_endpoint_api_call" in code
        assert "patch('requests.get')" in code
        assert "mock_get.return_value.status_code = 200" in code
    
    def test_parametrized_test_generation(self):
        """Test parametrized test generation"""
        config = TestConfig(
            framework=TestFramework.PYTEST,
            test_type=TestType.UNIT,
            test_name="math_function",
            module_path="math_module",
            include_parametrize=True
        )
        
        generator = TestCodeGenerator(config)
        code = generator.generate()
        
        assert '@pytest.mark.parametrize("input_val,expected"' in code
        assert "def test_math_function_parametrized" in code
    
    def test_save_to_file(self):
        """Test saving generated code to file"""
        config = TestConfig(
            framework=TestFramework.PYTEST,
            test_type=TestType.UNIT,
            test_name="file_test",
            module_path="test_module"
        )
        
        generator = TestCodeGenerator(config)
        
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = os.path.join(tmpdir, "test_output.py")
            generator.save_to_file(output_path)
            
            assert os.path.exists(output_path)
            
            with open(output_path, 'r') as f:
                content = f.read()
                assert "import pytest" in content
                assert "def test_file_test" in content
    
    def test_generate_test_file_convenience_function(self):
        """Test the convenience function generate_test_file"""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = os.path.join(tmpdir, "test_convenience.py")
            
            code = generate_test_file(
                framework="pytest",
                test_type="unit",
                test_name="convenience_test",
                module_path="my_module",
                output_path=output_path,
                include_fixtures=True,
                include_mocks=True,
                include_parametrize=False
            )
            
            assert os.path.exists(output_path)
            assert "import pytest" in code
            assert "def test_convenience_test" in code
    
    def test_invalid_framework_raises_error(self):
        """Test that invalid framework raises ValueError"""
        # This test verifies error handling
        config = TestConfig(
            framework=TestFramework.PYTEST,  # Valid for construction
            test_type=TestType.UNIT,
            test_name="test",
            module_path="module"
        )
        
        generator = TestCodeGenerator(config)
        # Manually set invalid framework to test error handling
        generator.config.framework = "invalid_framework"
        
        with pytest.raises(ValueError, match="Unsupported framework"):
            generator.generate()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

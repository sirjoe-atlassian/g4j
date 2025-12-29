"""
Tests for the TestCodeGenerator module.
"""

import pytest
import os
import tempfile
from test_generator import TestCodeGenerator, FunctionInfo


class TestFunctionInfo:
    """Tests for FunctionInfo dataclass."""
    
    def test_function_info_creation(self):
        """Test creating a FunctionInfo object."""
        func_info = FunctionInfo(
            name="test_func",
            args=["arg1", "arg2"],
            docstring="Test function",
            return_annotation="int"
        )
        
        assert func_info.name == "test_func"
        assert func_info.args == ["arg1", "arg2"]
        assert func_info.docstring == "Test function"
        assert func_info.return_annotation == "int"


class TestTestCodeGenerator:
    """Tests for TestCodeGenerator class."""
    
    def test_init_default_framework(self):
        """Test initialization with default framework."""
        generator = TestCodeGenerator()
        assert generator.framework == "pytest"
    
    def test_init_unittest_framework(self):
        """Test initialization with unittest framework."""
        generator = TestCodeGenerator(framework="unittest")
        assert generator.framework == "unittest"
    
    def test_parse_source_file(self):
        """Test parsing a source file."""
        generator = TestCodeGenerator()
        functions = generator.parse_source_file("example_module.py")
        
        # Should find add, multiply, greet, __init__, calculate
        assert len(functions) == 5
        
        # Check that add function is parsed correctly
        add_func = next(f for f in functions if f.name == "add")
        assert add_func.args == ["a", "b"]
        assert "Add two numbers" in add_func.docstring
        assert add_func.return_annotation == "int"
    
    def test_generate_pytest_test(self):
        """Test generating a pytest test."""
        generator = TestCodeGenerator(framework="pytest")
        func_info = FunctionInfo(
            name="sample_func",
            args=["param1", "param2"],
            docstring="Sample function for testing",
            return_annotation="str"
        )
        
        test_code = generator.generate_pytest_test(func_info, "my_module")
        
        assert "def test_sample_func():" in test_code
        assert "sample_func(param1, param2)" in test_code
        assert "TODO" in test_code
        assert "Sample function" in test_code
    
    def test_generate_unittest_test(self):
        """Test generating a unittest test."""
        generator = TestCodeGenerator(framework="unittest")
        func_info = FunctionInfo(
            name="sample_func",
            args=["param1", "param2"],
            docstring="Sample function for testing",
            return_annotation="str"
        )
        
        test_code = generator.generate_unittest_test(func_info, "my_module")
        
        assert "def test_sample_func(self):" in test_code
        assert "sample_func(param1, param2)" in test_code
        assert "TODO" in test_code
        assert "self.assertEqual" in test_code
    
    def test_generate_test_file_pytest(self):
        """Test generating a complete pytest test file."""
        generator = TestCodeGenerator(framework="pytest")
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='_test.py', delete=False) as tmp:
            output_file = tmp.name
        
        try:
            generator.generate_test_file("example_module.py", output_file)
            
            # Verify file was created
            assert os.path.exists(output_file)
            
            # Verify content
            with open(output_file, 'r') as f:
                content = f.read()
            
            assert "import pytest" in content
            assert "def test_add():" in content
            assert "def test_multiply():" in content
            assert "def test_greet():" in content
        finally:
            if os.path.exists(output_file):
                os.remove(output_file)
    
    def test_generate_test_file_unittest(self):
        """Test generating a complete unittest test file."""
        generator = TestCodeGenerator(framework="unittest")
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='_test.py', delete=False) as tmp:
            output_file = tmp.name
        
        try:
            generator.generate_test_file("example_module.py", output_file)
            
            # Verify file was created
            assert os.path.exists(output_file)
            
            # Verify content
            with open(output_file, 'r') as f:
                content = f.read()
            
            assert "import unittest" in content
            assert "class TestModule(unittest.TestCase):" in content
            assert "def test_add(self):" in content
            assert "def setUp(self):" in content
            assert "if __name__ == '__main__':" in content
        finally:
            if os.path.exists(output_file):
                os.remove(output_file)
    
    def test_private_functions_skipped(self):
        """Test that private functions are skipped."""
        # Create a temporary source file with private functions
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as tmp:
            tmp.write("""
def public_func():
    pass

def _private_func():
    pass

def __special_func__():
    pass
""")
            source_file = tmp.name
        
        try:
            generator = TestCodeGenerator()
            functions = generator.parse_source_file(source_file)
            
            function_names = [f.name for f in functions]
            
            # Should include public and special methods, but not private
            assert "public_func" in function_names
            assert "_private_func" not in function_names
            assert "__special_func__" in function_names
        finally:
            if os.path.exists(source_file):
                os.remove(source_file)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

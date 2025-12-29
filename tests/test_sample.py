"""
Sample test cases demonstrating the test automation framework.
"""

import pytest
import sys
import os

# Add parent directory to path to import test_automation module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from test_automation import TestRunner, APITestHelper, UITestHelper


class TestAPIHelper:
    """Test cases for API testing helpers."""
    
    def test_status_code_assertion_pass(self):
        """Test that valid status code passes."""
        APITestHelper.assert_status_code(200, 200)
    
    def test_status_code_assertion_fail(self):
        """Test that invalid status code raises assertion."""
        with pytest.raises(AssertionError):
            APITestHelper.assert_status_code(404, 200)
    
    def test_response_contains_key_pass(self):
        """Test that response contains expected key."""
        response = {'status': 'ok', 'data': 'test'}
        APITestHelper.assert_response_contains(response, 'status')
    
    def test_response_contains_key_fail(self):
        """Test that missing key raises assertion."""
        response = {'status': 'ok'}
        with pytest.raises(AssertionError):
            APITestHelper.assert_response_contains(response, 'missing_key')
    
    def test_response_value_match(self):
        """Test that response value matches expected."""
        response = {'status': 'success', 'code': 200}
        APITestHelper.assert_response_value(response, 'status', 'success')


class TestUIHelper:
    """Test cases for UI testing helpers."""
    
    def test_element_present_pass(self):
        """Test that present element passes."""
        element = "mock_element"
        UITestHelper.assert_element_present(element)
    
    def test_element_present_fail(self):
        """Test that None element raises assertion."""
        with pytest.raises(AssertionError):
            UITestHelper.assert_element_present(None)
    
    def test_element_visible_pass(self):
        """Test that visible element passes."""
        UITestHelper.assert_element_visible(True)
    
    def test_element_visible_fail(self):
        """Test that non-visible element raises assertion."""
        with pytest.raises(AssertionError):
            UITestHelper.assert_element_visible(False)
    
    def test_text_equals_pass(self):
        """Test that matching text passes."""
        UITestHelper.assert_text_equals("Hello", "Hello")
    
    def test_text_equals_fail(self):
        """Test that non-matching text raises assertion."""
        with pytest.raises(AssertionError):
            UITestHelper.assert_text_equals("Hello", "World")


class TestTestRunner:
    """Test cases for TestRunner class."""
    
    def test_runner_initialization(self):
        """Test that TestRunner initializes correctly."""
        runner = TestRunner()
        assert runner.test_results == []
    
    def test_run_passing_test(self):
        """Test running a passing test."""
        runner = TestRunner()
        
        def sample_test():
            assert True
        
        result = runner.run_test("Sample Test", sample_test)
        assert result['status'] == 'PASS'
        assert result['test_name'] == 'Sample Test'
        assert result['error'] is None
    
    def test_run_failing_test(self):
        """Test running a failing test."""
        runner = TestRunner()
        
        def sample_test():
            assert False, "This test should fail"
        
        result = runner.run_test("Failing Test", sample_test)
        assert result['status'] == 'FAIL'
        assert 'This test should fail' in result['error']
    
    def test_get_summary(self):
        """Test getting test summary."""
        runner = TestRunner()
        
        def passing_test():
            assert True
        
        def failing_test():
            assert False
        
        runner.run_test("Pass 1", passing_test)
        runner.run_test("Pass 2", passing_test)
        runner.run_test("Fail 1", failing_test)
        
        summary = runner.get_summary()
        assert summary['total'] == 3
        assert summary['passed'] == 2
        assert summary['failed'] == 1
        assert summary['errors'] == 0
        assert summary['pass_rate'] == pytest.approx(66.67, rel=0.1)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

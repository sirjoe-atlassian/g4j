"""
Test Automation Framework
Generated for Jira issue DEV-4: Test automation generate code

This module provides a basic test automation framework with utilities for:
- Test case management
- Test execution
- Result reporting
- Assertions and validations
"""

import unittest
import time
from typing import List, Dict, Any, Callable
from datetime import datetime
from enum import Enum


class TestResult(Enum):
    """Enumeration for test results."""
    PASSED = "PASSED"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"
    ERROR = "ERROR"


class TestCase:
    """
    Represents a single test case with metadata and execution details.
    """
    
    def __init__(self, name: str, description: str = "", tags: List[str] = None):
        """
        Initialize a test case.
        
        Args:
            name: Name of the test case
            description: Description of what the test validates
            tags: List of tags for categorization
        """
        self.name = name
        self.description = description
        self.tags = tags or []
        self.result = None
        self.duration = 0.0
        self.error_message = None
        self.timestamp = None
    
    def execute(self, test_function: Callable) -> TestResult:
        """
        Execute the test case function.
        
        Args:
            test_function: The function containing test logic
            
        Returns:
            TestResult indicating the outcome
        """
        self.timestamp = datetime.now()
        start_time = time.time()
        
        try:
            test_function()
            self.result = TestResult.PASSED
        except AssertionError as e:
            self.result = TestResult.FAILED
            self.error_message = str(e)
        except Exception as e:
            self.result = TestResult.ERROR
            self.error_message = f"{type(e).__name__}: {str(e)}"
        finally:
            self.duration = time.time() - start_time
        
        return self.result
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert test case to dictionary representation."""
        return {
            "name": self.name,
            "description": self.description,
            "tags": self.tags,
            "result": self.result.value if self.result else None,
            "duration": self.duration,
            "error_message": self.error_message,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None
        }


class TestSuite:
    """
    Manages a collection of test cases and their execution.
    """
    
    def __init__(self, name: str, description: str = ""):
        """
        Initialize a test suite.
        
        Args:
            name: Name of the test suite
            description: Description of the test suite
        """
        self.name = name
        self.description = description
        self.test_cases: List[TestCase] = []
        self.start_time = None
        self.end_time = None
    
    def add_test(self, test_case: TestCase):
        """Add a test case to the suite."""
        self.test_cases.append(test_case)
    
    def run(self, tag_filter: List[str] = None) -> Dict[str, Any]:
        """
        Execute all test cases in the suite.
        
        Args:
            tag_filter: Optional list of tags to filter tests
            
        Returns:
            Dictionary containing execution results
        """
        self.start_time = datetime.now()
        results = {
            TestResult.PASSED: 0,
            TestResult.FAILED: 0,
            TestResult.SKIPPED: 0,
            TestResult.ERROR: 0
        }
        
        for test_case in self.test_cases:
            # Skip tests that don't match tag filter
            if tag_filter and not any(tag in test_case.tags for tag in tag_filter):
                test_case.result = TestResult.SKIPPED
                results[TestResult.SKIPPED] += 1
                continue
            
            # Execute test (implementation would call actual test function)
            result = test_case.result or TestResult.SKIPPED
            results[result] += 1
        
        self.end_time = datetime.now()
        
        return {
            "suite_name": self.name,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "duration": (self.end_time - self.start_time).total_seconds(),
            "results": {k.value: v for k, v in results.items()},
            "total_tests": len(self.test_cases)
        }
    
    def get_summary(self) -> str:
        """Get a formatted summary of test results."""
        if not self.start_time:
            return "Test suite has not been executed yet."
        
        passed = sum(1 for tc in self.test_cases if tc.result == TestResult.PASSED)
        failed = sum(1 for tc in self.test_cases if tc.result == TestResult.FAILED)
        skipped = sum(1 for tc in self.test_cases if tc.result == TestResult.SKIPPED)
        errors = sum(1 for tc in self.test_cases if tc.result == TestResult.ERROR)
        total = len(self.test_cases)
        
        return f"""
Test Suite: {self.name}
{'=' * 50}
Total Tests: {total}
Passed: {passed}
Failed: {failed}
Skipped: {skipped}
Errors: {errors}
Success Rate: {(passed/total*100 if total > 0 else 0):.1f}%
Duration: {(self.end_time - self.start_time).total_seconds():.2f}s
"""


class TestReporter:
    """
    Generates test execution reports in various formats.
    """
    
    @staticmethod
    def generate_html_report(test_suite: TestSuite, output_path: str):
        """
        Generate an HTML report of test results.
        
        Args:
            test_suite: The test suite to report on
            output_path: Path to save the HTML report
        """
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Test Report - {test_suite.name}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .header {{ background-color: #4CAF50; color: white; padding: 20px; }}
        .summary {{ margin: 20px 0; }}
        .test-case {{ border: 1px solid #ddd; margin: 10px 0; padding: 10px; }}
        .passed {{ background-color: #d4edda; }}
        .failed {{ background-color: #f8d7da; }}
        .error {{ background-color: #fff3cd; }}
        .skipped {{ background-color: #e2e3e5; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Test Report: {test_suite.name}</h1>
        <p>{test_suite.description}</p>
    </div>
    <div class="summary">
        {test_suite.get_summary()}
    </div>
    <div class="test-cases">
        <h2>Test Cases</h2>
"""
        
        for tc in test_suite.test_cases:
            result_class = tc.result.value.lower() if tc.result else "unknown"
            html_content += f"""
        <div class="test-case {result_class}">
            <h3>{tc.name} - {tc.result.value if tc.result else 'N/A'}</h3>
            <p>{tc.description}</p>
            <p><strong>Duration:</strong> {tc.duration:.3f}s</p>
            {f'<p><strong>Error:</strong> {tc.error_message}</p>' if tc.error_message else ''}
            <p><strong>Tags:</strong> {', '.join(tc.tags) if tc.tags else 'None'}</p>
        </div>
"""
        
        html_content += """
    </div>
</body>
</html>
"""
        
        with open(output_path, 'w') as f:
            f.write(html_content)


class CustomAssertions:
    """
    Custom assertion utilities for test automation.
    """
    
    @staticmethod
    def assert_in_range(value: float, min_val: float, max_val: float, message: str = ""):
        """Assert that a value is within a specified range."""
        if not (min_val <= value <= max_val):
            raise AssertionError(
                message or f"Value {value} is not in range [{min_val}, {max_val}]"
            )
    
    @staticmethod
    def assert_dict_contains(dictionary: Dict, expected_keys: List[str], message: str = ""):
        """Assert that a dictionary contains all expected keys."""
        missing_keys = [key for key in expected_keys if key not in dictionary]
        if missing_keys:
            raise AssertionError(
                message or f"Dictionary is missing keys: {missing_keys}"
            )
    
    @staticmethod
    def assert_list_contains(lst: List, expected_items: List, message: str = ""):
        """Assert that a list contains all expected items."""
        missing_items = [item for item in expected_items if item not in lst]
        if missing_items:
            raise AssertionError(
                message or f"List is missing items: {missing_items}"
            )
    
    @staticmethod
    def assert_response_time(duration: float, max_duration: float, message: str = ""):
        """Assert that an operation completed within the expected time."""
        if duration > max_duration:
            raise AssertionError(
                message or f"Response time {duration:.3f}s exceeds maximum {max_duration:.3f}s"
            )


# Example usage
if __name__ == "__main__":
    # Create a test suite
    suite = TestSuite("Sample Test Suite", "Demonstration of test automation framework")
    
    # Create and add test cases
    test1 = TestCase(
        "test_sample_addition",
        "Verify that basic addition works correctly",
        ["math", "basic"]
    )
    
    # Simulate test execution
    def sample_test():
        assert 1 + 1 == 2, "Addition failed"
    
    test1.execute(sample_test)
    suite.add_test(test1)
    
    test2 = TestCase(
        "test_range_validation",
        "Verify range validation works",
        ["validation", "basic"]
    )
    
    def range_test():
        CustomAssertions.assert_in_range(5, 1, 10)
    
    test2.execute(range_test)
    suite.add_test(test2)
    
    # Run the suite and print summary
    suite.run()
    print(suite.get_summary())

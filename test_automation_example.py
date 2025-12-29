"""
Example Test Cases using the Test Automation Framework
Generated for Jira issue DEV-4: Test automation generate code

This file demonstrates how to use the test automation framework with practical examples.
"""

from test_automation import (
    TestCase, TestSuite, TestResult, TestReporter, CustomAssertions
)
import time


def example_api_test():
    """Example of testing API response structure."""
    # Simulate API response
    api_response = {
        "status": "success",
        "data": {"id": 1, "name": "Test User"},
        "timestamp": "2025-01-01T00:00:00Z"
    }
    
    # Validate response structure
    CustomAssertions.assert_dict_contains(
        api_response,
        ["status", "data", "timestamp"],
        "API response missing required fields"
    )
    
    assert api_response["status"] == "success", "API call was not successful"


def example_performance_test():
    """Example of testing performance requirements."""
    start = time.time()
    
    # Simulate some operation
    time.sleep(0.05)  # Simulating 50ms operation
    
    duration = time.time() - start
    
    # Assert response time is acceptable
    CustomAssertions.assert_response_time(
        duration,
        0.1,  # Max 100ms
        "Operation took too long"
    )


def example_data_validation_test():
    """Example of testing data validation."""
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "age": 25
    }
    
    # Validate all required fields are present
    CustomAssertions.assert_dict_contains(
        user_data,
        ["username", "email", "age"]
    )
    
    # Validate age is in valid range
    CustomAssertions.assert_in_range(user_data["age"], 18, 120)


def example_list_validation_test():
    """Example of testing list contents."""
    permissions = ["read", "write", "execute", "delete"]
    
    # Validate required permissions are present
    CustomAssertions.assert_list_contains(
        permissions,
        ["read", "write"],
        "Missing required permissions"
    )


def example_failing_test():
    """Example of a test that will fail."""
    assert 1 + 1 == 3, "This test is designed to fail"


def main():
    """Run example test suite."""
    # Create test suite
    suite = TestSuite(
        "Example Test Suite",
        "Comprehensive examples of test automation framework usage"
    )
    
    # Create and execute test cases
    test_cases = [
        (
            "test_api_response_validation",
            "Verify API response has correct structure and data",
            ["api", "integration"],
            example_api_test
        ),
        (
            "test_operation_performance",
            "Verify operation completes within acceptable time",
            ["performance"],
            example_performance_test
        ),
        (
            "test_user_data_validation",
            "Verify user data contains all required fields",
            ["validation", "data"],
            example_data_validation_test
        ),
        (
            "test_permission_list_validation",
            "Verify permission list contains required permissions",
            ["validation", "security"],
            example_list_validation_test
        ),
        (
            "test_intentional_failure",
            "This test demonstrates failure handling",
            ["demo", "negative"],
            example_failing_test
        ),
    ]
    
    for name, description, tags, test_func in test_cases:
        test_case = TestCase(name, description, tags)
        test_case.execute(test_func)
        suite.add_test(test_case)
    
    # Run suite and generate reports
    suite.run()
    
    # Print summary to console
    print(suite.get_summary())
    
    # Print detailed results
    print("\nDetailed Test Results:")
    print("=" * 70)
    for tc in suite.test_cases:
        status_symbol = "✓" if tc.result == TestResult.PASSED else "✗"
        print(f"{status_symbol} {tc.name} - {tc.result.value} ({tc.duration:.3f}s)")
        if tc.error_message:
            print(f"  Error: {tc.error_message}")
    
    # Generate HTML report
    TestReporter.generate_html_report(suite, "test_report.html")
    print("\nHTML report generated: test_report.html")
    
    # Return exit code based on results
    failed_count = sum(1 for tc in suite.test_cases 
                      if tc.result in [TestResult.FAILED, TestResult.ERROR])
    return 0 if failed_count == 0 else 1


if __name__ == "__main__":
    exit(main())

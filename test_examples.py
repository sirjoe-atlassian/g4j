"""
Example Test Cases using the Test Automation Framework
Demonstrates various testing scenarios and patterns.
"""

from test_automation_framework import TestCase, TestSuite, TestGenerator, TestStatus


def example_calculator_tests():
    """Example tests for a calculator application."""
    suite = TestSuite("Calculator Tests")
    
    # Test addition
    add_test = TestCase("test_addition", "Test calculator addition function")
    add_test.add_test_step(lambda: print("    Testing: 2 + 3 = 5"))
    add_test.add_test_step(lambda: None)  # Simulates assertion
    suite.add_test(add_test)
    
    # Test subtraction
    sub_test = TestCase("test_subtraction", "Test calculator subtraction function")
    sub_test.add_test_step(lambda: print("    Testing: 10 - 4 = 6"))
    sub_test.add_test_step(lambda: None)
    suite.add_test(sub_test)
    
    # Test division by zero (should handle gracefully)
    div_test = TestCase("test_division_by_zero", "Test division by zero handling")
    div_test.add_test_step(lambda: print("    Testing: 5 / 0 should raise error"))
    div_test.add_test_step(lambda: None)
    suite.add_test(div_test)
    
    return suite


def example_user_management_tests():
    """Example tests for user management system."""
    suite = TestSuite("User Management Tests")
    
    # Test user creation
    create_user_test = TestCase("test_create_user", "Test creating a new user")
    create_user_test.add_setup(lambda: print("    Setup: Connect to database"))
    create_user_test.add_test_step(lambda: print("    Action: Create user with valid data"))
    create_user_test.add_test_step(lambda: print("    Verify: User exists in database"))
    create_user_test.add_teardown(lambda: print("    Teardown: Clean up test data"))
    suite.add_test(create_user_test)
    
    # Test user authentication
    auth_test = TestCase("test_user_authentication", "Test user login authentication")
    auth_test.add_test_step(lambda: print("    Action: Attempt login with valid credentials"))
    auth_test.add_test_step(lambda: print("    Verify: Authentication successful"))
    suite.add_test(auth_test)
    
    # Test invalid authentication
    invalid_auth_test = TestCase("test_invalid_authentication", "Test login with invalid credentials")
    invalid_auth_test.add_test_step(lambda: print("    Action: Attempt login with invalid credentials"))
    invalid_auth_test.add_test_step(lambda: print("    Verify: Authentication fails gracefully"))
    suite.add_test(invalid_auth_test)
    
    return suite


def example_api_tests():
    """Example tests for REST API endpoints."""
    suite = TestSuite("API Integration Tests")
    
    # Generate API tests using the test generator
    endpoints = [
        ("/api/users", "GET", 200),
        ("/api/users", "POST", 201),
        ("/api/users/123", "GET", 200),
        ("/api/users/123", "PUT", 200),
        ("/api/users/123", "DELETE", 204),
    ]
    
    for endpoint, method, status_code in endpoints:
        test = TestGenerator.generate_api_test(endpoint, method, status_code)
        suite.add_test(test)
    
    return suite


def example_database_tests():
    """Example tests for database operations."""
    suite = TestSuite("Database Tests")
    
    # Test database connection
    conn_test = TestCase("test_database_connection", "Test database connectivity")
    conn_test.add_setup(lambda: print("    Setup: Initialize database connection"))
    conn_test.add_test_step(lambda: print("    Action: Execute test query"))
    conn_test.add_test_step(lambda: print("    Verify: Connection is active"))
    conn_test.add_teardown(lambda: print("    Teardown: Close connection"))
    suite.add_test(conn_test)
    
    # Test CRUD operations
    crud_test = TestCase("test_crud_operations", "Test Create, Read, Update, Delete")
    crud_test.add_test_step(lambda: print("    Action: Insert test record"))
    crud_test.add_test_step(lambda: print("    Verify: Record inserted"))
    crud_test.add_test_step(lambda: print("    Action: Read test record"))
    crud_test.add_test_step(lambda: print("    Verify: Record retrieved"))
    crud_test.add_test_step(lambda: print("    Action: Update test record"))
    crud_test.add_test_step(lambda: print("    Verify: Record updated"))
    crud_test.add_test_step(lambda: print("    Action: Delete test record"))
    crud_test.add_test_step(lambda: print("    Verify: Record deleted"))
    suite.add_test(crud_test)
    
    return suite


def example_integration_tests():
    """Example integration tests between components."""
    suite = TestSuite("Integration Tests")
    
    # Generate integration tests
    components = [
        ("Database", "API"),
        ("API", "Frontend"),
        ("Authentication", "Authorization"),
        ("Cache", "Database"),
    ]
    
    for component_a, component_b in components:
        test = TestGenerator.generate_integration_test(component_a, component_b)
        suite.add_test(test)
    
    return suite


def run_all_examples():
    """Run all example test suites."""
    print("\n" + "="*80)
    print("RUNNING ALL EXAMPLE TEST SUITES")
    print("="*80)
    
    all_suites = [
        example_calculator_tests(),
        example_user_management_tests(),
        example_api_tests(),
        example_database_tests(),
        example_integration_tests(),
    ]
    
    all_results = []
    for suite in all_suites:
        results = suite.run()
        all_results.extend(results)
        suite.export_results(f"{suite.name.lower().replace(' ', '_')}_results.json")
    
    # Print overall summary
    print("\n" + "="*80)
    print("OVERALL TEST EXECUTION SUMMARY")
    print("="*80)
    
    total_tests = len(all_results)
    passed = sum(1 for r in all_results if r.status == TestStatus.PASSED)
    failed = sum(1 for r in all_results if r.status == TestStatus.FAILED)
    errors = sum(1 for r in all_results if r.status == TestStatus.ERROR)
    
    print(f"Total Test Suites: {len(all_suites)}")
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed} ({passed/total_tests*100:.1f}%)")
    print(f"Failed: {failed}")
    print(f"Errors: {errors}")
    print("="*80 + "\n")


if __name__ == "__main__":
    run_all_examples()

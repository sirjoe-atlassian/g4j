"""
Example usage of the Test Automation Code Generator

This script demonstrates how to use the test generator to create
test files for different frameworks and test types.
"""

from test_automation_generator import (
    TestCodeGenerator,
    TestConfig,
    TestFramework,
    TestType,
    generate_test_file
)
import os


def example_pytest_unit_test():
    """Generate a pytest unit test"""
    print("=" * 60)
    print("Example 1: Pytest Unit Test")
    print("=" * 60)
    
    config = TestConfig(
        framework=TestFramework.PYTEST,
        test_type=TestType.UNIT,
        test_name="calculator_add",
        module_path="calculator",
        include_fixtures=True,
        include_mocks=False,
        include_parametrize=True
    )
    
    generator = TestCodeGenerator(config)
    code = generator.generate()
    print(code)
    print("\n")


def example_unittest_api_test():
    """Generate a unittest API test"""
    print("=" * 60)
    print("Example 2: Unittest API Test")
    print("=" * 60)
    
    config = TestConfig(
        framework=TestFramework.UNITTEST,
        test_type=TestType.API,
        test_name="user_api",
        module_path="api.users",
        include_fixtures=True,
        include_mocks=True,
        include_parametrize=False
    )
    
    generator = TestCodeGenerator(config)
    code = generator.generate()
    print(code)
    print("\n")


def example_jest_integration_test():
    """Generate a Jest integration test"""
    print("=" * 60)
    print("Example 3: Jest Integration Test")
    print("=" * 60)
    
    config = TestConfig(
        framework=TestFramework.JEST,
        test_type=TestType.INTEGRATION,
        test_name="user_service",
        module_path="./services/userService",
        include_fixtures=True,
        include_mocks=True,
        include_parametrize=True
    )
    
    generator = TestCodeGenerator(config)
    code = generator.generate()
    print(code)
    print("\n")


def example_junit_e2e_test():
    """Generate a JUnit E2E test"""
    print("=" * 60)
    print("Example 4: JUnit E2E Test")
    print("=" * 60)
    
    config = TestConfig(
        framework=TestFramework.JUNIT,
        test_type=TestType.E2E,
        test_name="checkout_flow",
        module_path="com.example.ecommerce",
        include_fixtures=True,
        include_mocks=True,
        include_parametrize=True
    )
    
    generator = TestCodeGenerator(config)
    code = generator.generate()
    print(code)
    print("\n")


def example_save_to_files():
    """Generate and save multiple test files"""
    print("=" * 60)
    print("Example 5: Generating and Saving Test Files")
    print("=" * 60)
    
    # Create output directory
    output_dir = "tmp_rovodev_generated_tests"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate multiple test files
    test_configs = [
        {
            "framework": "pytest",
            "test_type": "unit",
            "test_name": "string_utils",
            "module_path": "utils.strings",
            "output_path": f"{output_dir}/test_string_utils.py"
        },
        {
            "framework": "unittest",
            "test_type": "integration",
            "test_name": "database_connection",
            "module_path": "database.connection",
            "output_path": f"{output_dir}/test_database_connection.py"
        },
        {
            "framework": "jest",
            "test_type": "unit",
            "test_name": "auth_service",
            "module_path": "./services/auth",
            "output_path": f"{output_dir}/authService.test.js"
        },
    ]
    
    for config in test_configs:
        print(f"Generating: {config['output_path']}")
        generate_test_file(
            framework=config["framework"],
            test_type=config["test_type"],
            test_name=config["test_name"],
            module_path=config["module_path"],
            output_path=config["output_path"],
            include_fixtures=True,
            include_mocks=True,
            include_parametrize=False
        )
        print(f"✓ Created: {config['output_path']}")
    
    print(f"\nAll test files generated in '{output_dir}/' directory")
    print("\n")


def main():
    """Run all examples"""
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 10 + "Test Automation Code Generator Examples" + " " * 9 + "║")
    print("╚" + "═" * 58 + "╝")
    print("\n")
    
    # Run examples
    example_pytest_unit_test()
    example_unittest_api_test()
    example_jest_integration_test()
    example_junit_e2e_test()
    example_save_to_files()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

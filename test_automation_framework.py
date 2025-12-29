"""
Test Automation Framework
A comprehensive testing framework for automated test generation and execution.
"""

import unittest
import json
import time
from typing import Dict, List, Any, Callable
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class TestStatus(Enum):
    """Test execution status enumeration."""
    PASSED = "PASSED"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"
    ERROR = "ERROR"


@dataclass
class TestResult:
    """Data class to store test execution results."""
    test_name: str
    status: TestStatus
    duration: float
    error_message: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert test result to dictionary."""
        return {
            "test_name": self.test_name,
            "status": self.status.value,
            "duration": self.duration,
            "error_message": self.error_message,
            "timestamp": self.timestamp
        }


class TestCase:
    """Base class for automated test cases."""
    
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.setup_actions: List[Callable] = []
        self.test_actions: List[Callable] = []
        self.teardown_actions: List[Callable] = []
        
    def add_setup(self, action: Callable) -> 'TestCase':
        """Add a setup action to be executed before the test."""
        self.setup_actions.append(action)
        return self
    
    def add_test_step(self, action: Callable) -> 'TestCase':
        """Add a test step to be executed during the test."""
        self.test_actions.append(action)
        return self
    
    def add_teardown(self, action: Callable) -> 'TestCase':
        """Add a teardown action to be executed after the test."""
        self.teardown_actions.append(action)
        return self
    
    def execute(self) -> TestResult:
        """Execute the test case and return the result."""
        start_time = time.time()
        status = TestStatus.PASSED
        error_message = ""
        
        try:
            # Execute setup actions
            for action in self.setup_actions:
                action()
            
            # Execute test actions
            for action in self.test_actions:
                action()
                
        except AssertionError as e:
            status = TestStatus.FAILED
            error_message = str(e)
        except Exception as e:
            status = TestStatus.ERROR
            error_message = f"{type(e).__name__}: {str(e)}"
        finally:
            # Execute teardown actions
            try:
                for action in self.teardown_actions:
                    action()
            except Exception as e:
                if status == TestStatus.PASSED:
                    status = TestStatus.ERROR
                    error_message = f"Teardown error: {str(e)}"
        
        duration = time.time() - start_time
        return TestResult(
            test_name=self.name,
            status=status,
            duration=duration,
            error_message=error_message
        )


class TestSuite:
    """Collection of test cases to be executed together."""
    
    def __init__(self, name: str):
        self.name = name
        self.test_cases: List[TestCase] = []
        self.results: List[TestResult] = []
        
    def add_test(self, test_case: TestCase) -> 'TestSuite':
        """Add a test case to the suite."""
        self.test_cases.append(test_case)
        return self
    
    def run(self) -> List[TestResult]:
        """Execute all test cases in the suite."""
        self.results = []
        print(f"\n{'='*60}")
        print(f"Running Test Suite: {self.name}")
        print(f"{'='*60}")
        
        for test_case in self.test_cases:
            print(f"\nExecuting: {test_case.name}")
            if test_case.description:
                print(f"  Description: {test_case.description}")
            
            result = test_case.execute()
            self.results.append(result)
            
            print(f"  Status: {result.status.value}")
            print(f"  Duration: {result.duration:.4f}s")
            if result.error_message:
                print(f"  Error: {result.error_message}")
        
        self._print_summary()
        return self.results
    
    def _print_summary(self):
        """Print test execution summary."""
        print(f"\n{'='*60}")
        print("Test Summary")
        print(f"{'='*60}")
        
        passed = sum(1 for r in self.results if r.status == TestStatus.PASSED)
        failed = sum(1 for r in self.results if r.status == TestStatus.FAILED)
        errors = sum(1 for r in self.results if r.status == TestStatus.ERROR)
        skipped = sum(1 for r in self.results if r.status == TestStatus.SKIPPED)
        total = len(self.results)
        
        print(f"Total Tests: {total}")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        print(f"Errors: {errors}")
        print(f"Skipped: {skipped}")
        print(f"{'='*60}\n")
    
    def export_results(self, filename: str = "test_results.json"):
        """Export test results to a JSON file."""
        results_data = {
            "suite_name": self.name,
            "total_tests": len(self.results),
            "timestamp": datetime.now().isoformat(),
            "results": [result.to_dict() for result in self.results]
        }
        
        with open(filename, 'w') as f:
            json.dump(results_data, f, indent=2)
        
        print(f"Results exported to {filename}")


class TestGenerator:
    """Utility class to generate test cases programmatically."""
    
    @staticmethod
    def generate_api_test(endpoint: str, method: str, expected_status: int) -> TestCase:
        """Generate a test case for API endpoint testing."""
        test = TestCase(
            name=f"test_{method.lower()}_{endpoint.replace('/', '_')}",
            description=f"Test {method} request to {endpoint}"
        )
        
        def api_call():
            # Placeholder for actual API call
            print(f"    Making {method} request to {endpoint}")
            # assert response.status_code == expected_status
        
        test.add_test_step(api_call)
        return test
    
    @staticmethod
    def generate_unit_test(function_name: str, inputs: List[Any], expected_output: Any) -> TestCase:
        """Generate a unit test for a function."""
        test = TestCase(
            name=f"test_{function_name}",
            description=f"Unit test for {function_name} with inputs {inputs}"
        )
        
        def unit_test():
            # Placeholder for actual function call
            print(f"    Testing {function_name} with inputs: {inputs}")
            # result = target_function(*inputs)
            # assert result == expected_output
        
        test.add_test_step(unit_test)
        return test
    
    @staticmethod
    def generate_integration_test(component_a: str, component_b: str) -> TestCase:
        """Generate an integration test between two components."""
        test = TestCase(
            name=f"test_integration_{component_a}_{component_b}",
            description=f"Integration test between {component_a} and {component_b}"
        )
        
        def integration_test():
            print(f"    Testing integration between {component_a} and {component_b}")
            # Placeholder for actual integration test logic
        
        test.add_test_step(integration_test)
        return test


# Example usage and demonstration
def demo_test_automation():
    """Demonstrate the test automation framework."""
    
    # Create a test suite
    suite = TestSuite("Demo Test Suite")
    
    # Create manual test case
    custom_test = TestCase("test_custom_logic", "A custom test with multiple steps")
    custom_test.add_setup(lambda: print("    Setup: Initializing test environment"))
    custom_test.add_test_step(lambda: print("    Step 1: Performing action A"))
    custom_test.add_test_step(lambda: print("    Step 2: Verifying result"))
    custom_test.add_teardown(lambda: print("    Teardown: Cleaning up"))
    
    suite.add_test(custom_test)
    
    # Generate API tests
    api_test1 = TestGenerator.generate_api_test("/api/users", "GET", 200)
    api_test2 = TestGenerator.generate_api_test("/api/users/1", "POST", 201)
    
    suite.add_test(api_test1)
    suite.add_test(api_test2)
    
    # Generate unit tests
    unit_test1 = TestGenerator.generate_unit_test("add", [2, 3], 5)
    unit_test2 = TestGenerator.generate_unit_test("multiply", [4, 5], 20)
    
    suite.add_test(unit_test1)
    suite.add_test(unit_test2)
    
    # Generate integration test
    integration_test = TestGenerator.generate_integration_test("Database", "API")
    suite.add_test(integration_test)
    
    # Run the test suite
    results = suite.run()
    
    # Export results
    suite.export_results("demo_test_results.json")
    
    return results


if __name__ == "__main__":
    print("Test Automation Framework Demo")
    print("="*60)
    demo_test_automation()

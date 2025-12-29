#!/usr/bin/env python3
"""
Test Automation Framework for g4j Project
This framework provides a comprehensive testing solution with unit, integration, and E2E capabilities.
"""

import unittest
import json
import time
from typing import Any, Dict, List, Optional
from datetime import datetime
from dataclasses import dataclass, asdict
from abc import ABC, abstractmethod


@dataclass
class TestResult:
    """Data class to store test execution results"""
    test_name: str
    status: str  # 'PASS', 'FAIL', 'SKIP'
    execution_time: float
    error_message: Optional[str] = None
    timestamp: str = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().isoformat()


class TestReporter:
    """Generates test reports in multiple formats"""
    
    def __init__(self):
        self.results: List[TestResult] = []
    
    def add_result(self, result: TestResult):
        """Add a test result to the reporter"""
        self.results.append(result)
    
    def generate_json_report(self, filename: str = "test_report.json"):
        """Generate JSON format test report"""
        report = {
            "total_tests": len(self.results),
            "passed": sum(1 for r in self.results if r.status == "PASS"),
            "failed": sum(1 for r in self.results if r.status == "FAIL"),
            "skipped": sum(1 for r in self.results if r.status == "SKIP"),
            "total_execution_time": sum(r.execution_time for r in self.results),
            "tests": [asdict(r) for r in self.results]
        }
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        
        return report
    
    def generate_console_report(self) -> str:
        """Generate human-readable console report"""
        total = len(self.results)
        passed = sum(1 for r in self.results if r.status == "PASS")
        failed = sum(1 for r in self.results if r.status == "FAIL")
        skipped = sum(1 for r in self.results if r.status == "SKIP")
        
        report = f"""
{'='*60}
TEST EXECUTION REPORT
{'='*60}
Total Tests: {total}
Passed: {passed} ✓
Failed: {failed} ✗
Skipped: {skipped} ⊘
Success Rate: {(passed/total*100) if total > 0 else 0:.2f}%
{'='*60}
"""
        
        if failed > 0:
            report += "\nFailed Tests:\n"
            for result in self.results:
                if result.status == "FAIL":
                    report += f"  - {result.test_name}: {result.error_message}\n"
        
        return report


class BaseTestCase(ABC):
    """Abstract base class for all test cases"""
    
    def __init__(self, name: str):
        self.name = name
        self.setup_done = False
    
    def setup(self):
        """Setup method to be overridden by subclasses"""
        pass
    
    def teardown(self):
        """Teardown method to be overridden by subclasses"""
        pass
    
    @abstractmethod
    def run(self) -> TestResult:
        """Execute the test case"""
        pass


class UnitTestCase(BaseTestCase):
    """Unit test case implementation"""
    
    def __init__(self, name: str, test_func):
        super().__init__(name)
        self.test_func = test_func
    
    def run(self) -> TestResult:
        """Execute the unit test"""
        start_time = time.time()
        
        try:
            self.setup()
            self.test_func()
            execution_time = time.time() - start_time
            return TestResult(
                test_name=self.name,
                status="PASS",
                execution_time=execution_time
            )
        except AssertionError as e:
            execution_time = time.time() - start_time
            return TestResult(
                test_name=self.name,
                status="FAIL",
                execution_time=execution_time,
                error_message=str(e)
            )
        except Exception as e:
            execution_time = time.time() - start_time
            return TestResult(
                test_name=self.name,
                status="FAIL",
                execution_time=execution_time,
                error_message=f"Unexpected error: {str(e)}"
            )
        finally:
            self.teardown()


class IntegrationTestCase(BaseTestCase):
    """Integration test case implementation"""
    
    def __init__(self, name: str, test_func, dependencies: List[str] = None):
        super().__init__(name)
        self.test_func = test_func
        self.dependencies = dependencies or []
    
    def run(self) -> TestResult:
        """Execute the integration test"""
        start_time = time.time()
        
        try:
            self.setup()
            self.test_func()
            execution_time = time.time() - start_time
            return TestResult(
                test_name=self.name,
                status="PASS",
                execution_time=execution_time
            )
        except AssertionError as e:
            execution_time = time.time() - start_time
            return TestResult(
                test_name=self.name,
                status="FAIL",
                execution_time=execution_time,
                error_message=str(e)
            )
        except Exception as e:
            execution_time = time.time() - start_time
            return TestResult(
                test_name=self.name,
                status="FAIL",
                execution_time=execution_time,
                error_message=f"Unexpected error: {str(e)}"
            )
        finally:
            self.teardown()


class TestSuite:
    """Test suite to organize and execute multiple test cases"""
    
    def __init__(self, name: str):
        self.name = name
        self.test_cases: List[BaseTestCase] = []
        self.reporter = TestReporter()
    
    def add_test(self, test_case: BaseTestCase):
        """Add a test case to the suite"""
        self.test_cases.append(test_case)
    
    def run_all(self) -> TestReporter:
        """Execute all test cases in the suite"""
        print(f"\nRunning Test Suite: {self.name}")
        print("=" * 60)
        
        for test_case in self.test_cases:
            print(f"Executing: {test_case.name}...", end=" ")
            result = test_case.run()
            self.reporter.add_result(result)
            
            status_symbol = "✓" if result.status == "PASS" else "✗"
            print(f"{status_symbol} ({result.execution_time:.3f}s)")
        
        print(self.reporter.generate_console_report())
        return self.reporter


class TestRunner:
    """Main test runner to coordinate test execution"""
    
    def __init__(self):
        self.suites: List[TestSuite] = []
    
    def add_suite(self, suite: TestSuite):
        """Add a test suite to the runner"""
        self.suites.append(suite)
    
    def run_all_suites(self):
        """Execute all test suites"""
        print("\n" + "=" * 60)
        print("STARTING TEST AUTOMATION")
        print("=" * 60)
        
        all_results = []
        for suite in self.suites:
            reporter = suite.run_all()
            all_results.extend(reporter.results)
        
        # Generate final consolidated report
        final_reporter = TestReporter()
        final_reporter.results = all_results
        final_reporter.generate_json_report("final_test_report.json")
        
        print("\n" + "=" * 60)
        print("ALL TESTS COMPLETED")
        print("=" * 60)
        print(f"Report saved to: final_test_report.json")


# Example usage and sample tests
if __name__ == "__main__":
    # Create test runner
    runner = TestRunner()
    
    # Create unit test suite
    unit_suite = TestSuite("Unit Tests")
    
    # Sample unit tests
    def test_addition():
        assert 2 + 2 == 4, "Addition failed"
    
    def test_subtraction():
        assert 5 - 3 == 2, "Subtraction failed"
    
    def test_string_operations():
        assert "hello".upper() == "HELLO", "String upper case failed"
    
    unit_suite.add_test(UnitTestCase("Test Addition", test_addition))
    unit_suite.add_test(UnitTestCase("Test Subtraction", test_subtraction))
    unit_suite.add_test(UnitTestCase("Test String Operations", test_string_operations))
    
    # Create integration test suite
    integration_suite = TestSuite("Integration Tests")
    
    def test_data_pipeline():
        data = [1, 2, 3, 4, 5]
        result = sum(data)
        assert result == 15, f"Expected 15, got {result}"
    
    def test_json_processing():
        test_data = {"name": "test", "value": 123}
        json_str = json.dumps(test_data)
        parsed = json.loads(json_str)
        assert parsed == test_data, "JSON processing failed"
    
    integration_suite.add_test(IntegrationTestCase("Test Data Pipeline", test_data_pipeline))
    integration_suite.add_test(IntegrationTestCase("Test JSON Processing", test_json_processing))
    
    # Add suites to runner
    runner.add_suite(unit_suite)
    runner.add_suite(integration_suite)
    
    # Execute all tests
    runner.run_all_suites()

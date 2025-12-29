"""
Test Automation Framework
A generic test automation framework with utilities and base classes
for automated testing.
"""

import unittest
import logging
import json
from datetime import datetime
from typing import Dict, List, Any, Optional
from abc import ABC, abstractmethod


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class TestReport:
    """Class to generate test execution reports"""
    
    def __init__(self):
        self.results: List[Dict[str, Any]] = []
        self.start_time = datetime.now()
        
    def add_result(self, test_name: str, status: str, duration: float, 
                   error_message: Optional[str] = None):
        """Add a test result to the report"""
        self.results.append({
            'test_name': test_name,
            'status': status,
            'duration': duration,
            'error_message': error_message,
            'timestamp': datetime.now().isoformat()
        })
        
    def generate_summary(self) -> Dict[str, Any]:
        """Generate a summary of test results"""
        total = len(self.results)
        passed = sum(1 for r in self.results if r['status'] == 'PASSED')
        failed = sum(1 for r in self.results if r['status'] == 'FAILED')
        skipped = sum(1 for r in self.results if r['status'] == 'SKIPPED')
        
        return {
            'total_tests': total,
            'passed': passed,
            'failed': failed,
            'skipped': skipped,
            'pass_rate': f"{(passed/total*100):.2f}%" if total > 0 else "0%",
            'execution_time': str(datetime.now() - self.start_time),
            'results': self.results
        }
        
    def save_report(self, filename: str = 'test_report.json'):
        """Save the report to a JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.generate_summary(), f, indent=2)
        logger.info(f"Test report saved to {filename}")


class BaseTestCase(unittest.TestCase, ABC):
    """Base test case class with common setup and teardown"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test class - runs once before all tests"""
        logger.info(f"Setting up test class: {cls.__name__}")
        cls.test_report = TestReport()
        
    @classmethod
    def tearDownClass(cls):
        """Tear down test class - runs once after all tests"""
        logger.info(f"Tearing down test class: {cls.__name__}")
        summary = cls.test_report.generate_summary()
        logger.info(f"Test Summary: {summary['passed']}/{summary['total_tests']} passed")
        
    def setUp(self):
        """Set up individual test - runs before each test"""
        self.test_start_time = datetime.now()
        logger.info(f"Starting test: {self._testMethodName}")
        
    def tearDown(self):
        """Tear down individual test - runs after each test"""
        duration = (datetime.now() - self.test_start_time).total_seconds()
        result = self._outcome.result
        
        if result.errors and any(self._testMethodName in str(error[0]) for error in result.errors):
            status = 'ERROR'
            error_msg = str(result.errors[-1][1])
        elif result.failures and any(self._testMethodName in str(failure[0]) for failure in result.failures):
            status = 'FAILED'
            error_msg = str(result.failures[-1][1])
        elif result.skipped and any(self._testMethodName in str(skip[0]) for skip in result.skipped):
            status = 'SKIPPED'
            error_msg = None
        else:
            status = 'PASSED'
            error_msg = None
            
        self.test_report.add_result(self._testMethodName, status, duration, error_msg)
        logger.info(f"Test {self._testMethodName} completed: {status} ({duration:.2f}s)")


class APITestHelper:
    """Helper class for API testing"""
    
    @staticmethod
    def validate_response_status(response, expected_status: int):
        """Validate API response status code"""
        assert response.status_code == expected_status, \
            f"Expected status {expected_status}, got {response.status_code}"
    
    @staticmethod
    def validate_json_schema(response_json: Dict, required_fields: List[str]):
        """Validate that JSON response contains required fields"""
        missing_fields = [field for field in required_fields if field not in response_json]
        assert not missing_fields, f"Missing required fields: {missing_fields}"
    
    @staticmethod
    def validate_response_time(duration: float, max_duration: float):
        """Validate API response time"""
        assert duration <= max_duration, \
            f"Response time {duration}s exceeded maximum {max_duration}s"


class DataValidator:
    """Helper class for data validation"""
    
    @staticmethod
    def validate_not_empty(value: Any, field_name: str = "Field"):
        """Validate that a value is not empty"""
        assert value, f"{field_name} should not be empty"
    
    @staticmethod
    def validate_type(value: Any, expected_type: type, field_name: str = "Field"):
        """Validate that a value is of expected type"""
        assert isinstance(value, expected_type), \
            f"{field_name} should be of type {expected_type.__name__}, got {type(value).__name__}"
    
    @staticmethod
    def validate_range(value: float, min_value: float, max_value: float, 
                      field_name: str = "Field"):
        """Validate that a numeric value is within range"""
        assert min_value <= value <= max_value, \
            f"{field_name} value {value} is not within range [{min_value}, {max_value}]"
    
    @staticmethod
    def validate_regex(value: str, pattern: str, field_name: str = "Field"):
        """Validate that a string matches a regex pattern"""
        import re
        assert re.match(pattern, value), \
            f"{field_name} value '{value}' does not match pattern '{pattern}'"


class TestDataGenerator:
    """Helper class to generate test data"""
    
    @staticmethod
    def generate_test_user(user_id: int = 1) -> Dict[str, Any]:
        """Generate test user data"""
        return {
            'id': user_id,
            'username': f'testuser{user_id}',
            'email': f'testuser{user_id}@example.com',
            'first_name': f'Test',
            'last_name': f'User{user_id}',
            'is_active': True
        }
    
    @staticmethod
    def generate_test_data_set(count: int, data_type: str = 'user') -> List[Dict[str, Any]]:
        """Generate a set of test data"""
        if data_type == 'user':
            return [TestDataGenerator.generate_test_user(i) for i in range(1, count + 1)]
        return []


# Example test cases demonstrating the framework
class ExampleTestSuite(BaseTestCase):
    """Example test suite showing framework usage"""
    
    def test_example_pass(self):
        """Example test that passes"""
        self.assertEqual(1 + 1, 2, "Basic arithmetic should work")
        
    def test_example_data_validation(self):
        """Example test using data validation"""
        test_user = TestDataGenerator.generate_test_user()
        DataValidator.validate_not_empty(test_user['username'], 'Username')
        DataValidator.validate_type(test_user['id'], int, 'User ID')
        DataValidator.validate_regex(test_user['email'], r'^[\w\.-]+@[\w\.-]+\.\w+$', 'Email')
        
    def test_example_with_assertion(self):
        """Example test with custom assertion"""
        result = {'status': 'success', 'data': [1, 2, 3]}
        self.assertIn('status', result)
        self.assertEqual(result['status'], 'success')
        self.assertIsInstance(result['data'], list)
        self.assertGreater(len(result['data']), 0)


def run_test_suite(test_suite=None):
    """Run the test suite and generate report"""
    if test_suite is None:
        # Run all tests
        loader = unittest.TestLoader()
        test_suite = loader.loadTestsFromTestCase(ExampleTestSuite)
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    return result


if __name__ == '__main__':
    logger.info("Starting Test Automation Framework")
    result = run_test_suite()
    
    # Save report
    if hasattr(ExampleTestSuite, 'test_report'):
        ExampleTestSuite.test_report.save_report()
    
    # Exit with appropriate code
    exit(0 if result.wasSuccessful() else 1)

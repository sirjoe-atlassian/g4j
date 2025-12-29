"""
Test data management utilities.
"""
import json
import os
from typing import Dict, Any, List


class TestDataManager:
    """Manage test data for automation tests."""
    
    def __init__(self, data_dir: str = 'test_data'):
        """
        Initialize test data manager.
        
        Args:
            data_dir: Directory containing test data files
        """
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
    
    def load_json(self, filename: str) -> Dict[str, Any]:
        """
        Load test data from JSON file.
        
        Args:
            filename: JSON filename
        
        Returns:
            Dictionary containing test data
        """
        filepath = os.path.join(self.data_dir, filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f'Test data file not found: {filepath}')
        
        with open(filepath, 'r') as f:
            return json.load(f)
    
    def save_json(self, filename: str, data: Dict[str, Any]):
        """
        Save test data to JSON file.
        
        Args:
            filename: JSON filename
            data: Data to save
        """
        filepath = os.path.join(self.data_dir, filename)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
    
    def get_test_data(self, test_name: str) -> Dict[str, Any]:
        """
        Get test data for specific test.
        
        Args:
            test_name: Name of the test
        
        Returns:
            Test data dictionary
        """
        try:
            return self.load_json(f'{test_name}.json')
        except FileNotFoundError:
            return {}

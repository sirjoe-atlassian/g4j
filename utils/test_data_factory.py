"""Test data factory for generating test data."""
from faker import Faker
from typing import Dict, Any


class TestDataFactory:
    """Factory for generating test data using Faker."""
    
    def __init__(self):
        """Initialize the test data factory."""
        self.faker = Faker()
    
    def create_user_data(self) -> Dict[str, Any]:
        """Generate fake user data.
        
        Returns:
            Dictionary with user data
        """
        return {
            'first_name': self.faker.first_name(),
            'last_name': self.faker.last_name(),
            'email': self.faker.email(),
            'username': self.faker.user_name(),
            'password': self.faker.password(),
            'phone': self.faker.phone_number(),
            'address': self.create_address_data()
        }
    
    def create_address_data(self) -> Dict[str, str]:
        """Generate fake address data.
        
        Returns:
            Dictionary with address data
        """
        return {
            'street': self.faker.street_address(),
            'city': self.faker.city(),
            'state': self.faker.state(),
            'country': self.faker.country(),
            'postal_code': self.faker.postcode()
        }
    
    def create_company_data(self) -> Dict[str, str]:
        """Generate fake company data.
        
        Returns:
            Dictionary with company data
        """
        return {
            'name': self.faker.company(),
            'email': self.faker.company_email(),
            'phone': self.faker.phone_number(),
            'website': self.faker.url(),
            'address': self.create_address_data()
        }
    
    def create_product_data(self) -> Dict[str, Any]:
        """Generate fake product data.
        
        Returns:
            Dictionary with product data
        """
        return {
            'name': self.faker.word().title(),
            'description': self.faker.text(),
            'price': float(self.faker.random_int(min=10, max=1000)),
            'sku': self.faker.bothify(text='???-########'),
            'category': self.faker.word()
        }


# Singleton instance
test_data_factory = TestDataFactory()

"""
API Test Examples using pytest
Jira Issue: DEV-4 - Test automation generate code
"""

import pytest
import logging

logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.smoke
class TestUserAPI:
    """Test cases for User API endpoints"""
    
    def test_get_user_by_id(self, api_client):
        """Test retrieving a user by ID"""
        # Arrange
        user_id = 1
        
        # Act
        response = api_client.get(f'/users/{user_id}')
        
        # Assert
        assert response['status'] == 200
        logger.info(f"Successfully retrieved user {user_id}")
    
    def test_create_user(self, api_client, sample_user_data):
        """Test creating a new user"""
        # Act
        response = api_client.post('/users', sample_user_data)
        
        # Assert
        assert response['status'] == 201
        assert response['data']['username'] == sample_user_data['username']
        logger.info(f"Successfully created user: {sample_user_data['username']}")
    
    def test_get_all_users(self, api_client):
        """Test retrieving all users"""
        # Act
        response = api_client.get('/users')
        
        # Assert
        assert response['status'] == 200
        logger.info("Successfully retrieved all users")
    
    @pytest.mark.parametrize("user_id,expected_status", [
        (1, 200),
        (999, 404),
        (-1, 400),
    ])
    def test_get_user_various_ids(self, api_client, user_id, expected_status):
        """Test getting users with various IDs"""
        # Act
        response = api_client.get(f'/users/{user_id}')
        
        # Assert
        assert response['status'] == expected_status
        logger.info(f"User ID {user_id} returned status {expected_status}")


@pytest.mark.api
@pytest.mark.regression
class TestProductAPI:
    """Test cases for Product API endpoints"""
    
    def test_get_product_list(self, api_client):
        """Test retrieving product list"""
        # Act
        response = api_client.get('/products')
        
        # Assert
        assert response['status'] == 200
        logger.info("Successfully retrieved product list")
    
    def test_create_product(self, api_client):
        """Test creating a new product"""
        # Arrange
        product_data = {
            'name': 'Test Product',
            'price': 29.99,
            'in_stock': True
        }
        
        # Act
        response = api_client.post('/products', product_data)
        
        # Assert
        assert response['status'] == 201
        assert response['data']['name'] == product_data['name']
        logger.info(f"Successfully created product: {product_data['name']}")
    
    def test_search_products(self, api_client):
        """Test product search functionality"""
        # Arrange
        search_query = "test"
        
        # Act
        response = api_client.get(f'/products/search?q={search_query}')
        
        # Assert
        assert response['status'] == 200
        logger.info(f"Successfully searched products with query: {search_query}")

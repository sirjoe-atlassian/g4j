"""
Sample API tests for test automation framework.
"""
import pytest
from src.utils.api_client import APIClient


@pytest.mark.integration
class TestAPIClient:
    """Test API client functionality."""
    
    def test_api_client_initialization(self):
        """Test API client can be initialized."""
        client = APIClient('https://api.example.com', timeout=30)
        assert client.base_url == 'https://api.example.com'
        assert client.timeout == 30
        client.close()
    
    def test_api_client_set_auth_token(self):
        """Test setting authentication token."""
        client = APIClient('https://api.example.com')
        client.set_auth_token('test_token_123')
        assert 'Authorization' in client.headers
        assert client.headers['Authorization'] == 'Bearer test_token_123'
        client.close()
    
    def test_api_client_custom_token_type(self):
        """Test setting custom token type."""
        client = APIClient('https://api.example.com')
        client.set_auth_token('test_token_123', token_type='Token')
        assert client.headers['Authorization'] == 'Token test_token_123'
        client.close()


@pytest.mark.integration
class TestJSONPlaceholderAPI:
    """
    Test against JSONPlaceholder - a free fake API for testing.
    These tests demonstrate real API testing scenarios.
    """
    
    @pytest.fixture(scope='class')
    def json_api(self):
        """Provide API client for JSONPlaceholder."""
        client = APIClient('https://jsonplaceholder.typicode.com')
        yield client
        client.close()
    
    def test_get_users(self, json_api):
        """Test getting list of users."""
        response = json_api.get('/users')
        assert response.status_code == 200
        users = response.json()
        assert isinstance(users, list)
        assert len(users) > 0
    
    def test_get_single_user(self, json_api):
        """Test getting a single user."""
        response = json_api.get('/users/1')
        assert response.status_code == 200
        user = response.json()
        assert 'id' in user
        assert user['id'] == 1
        assert 'name' in user
        assert 'email' in user
    
    def test_get_posts(self, json_api):
        """Test getting list of posts."""
        response = json_api.get('/posts')
        assert response.status_code == 200
        posts = response.json()
        assert isinstance(posts, list)
        assert len(posts) > 0
    
    def test_create_post(self, json_api):
        """Test creating a new post."""
        new_post = {
            'title': 'Test Post',
            'body': 'This is a test post',
            'userId': 1
        }
        response = json_api.post('/posts', json=new_post)
        assert response.status_code == 201
        created_post = response.json()
        assert created_post['title'] == new_post['title']
        assert created_post['body'] == new_post['body']
    
    def test_update_post(self, json_api):
        """Test updating an existing post."""
        updated_post = {
            'id': 1,
            'title': 'Updated Title',
            'body': 'Updated body',
            'userId': 1
        }
        response = json_api.put('/posts/1', json=updated_post)
        assert response.status_code == 200
        result = response.json()
        assert result['title'] == updated_post['title']
    
    def test_delete_post(self, json_api):
        """Test deleting a post."""
        response = json_api.delete('/posts/1')
        assert response.status_code == 200
    
    def test_get_user_posts(self, json_api):
        """Test getting posts for a specific user."""
        response = json_api.get('/posts', params={'userId': 1})
        assert response.status_code == 200
        posts = response.json()
        assert isinstance(posts, list)
        # Verify all posts belong to user 1
        for post in posts:
            assert post['userId'] == 1
    
    def test_invalid_endpoint_returns_404(self, json_api):
        """Test that invalid endpoint returns 404."""
        response = json_api.get('/invalid_endpoint_xyz')
        assert response.status_code == 404

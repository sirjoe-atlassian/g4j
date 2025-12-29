#!/usr/bin/env python3
"""
API Test Examples
This module contains example API test cases using the API test helper.
"""

import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from test_automation.api_test_helper import APITestHelper


class TestJSONPlaceholderAPI(unittest.TestCase):
    """Test cases for JSONPlaceholder API (example public API)."""
    
    @classmethod
    def setUpClass(cls):
        """Set up test class - runs once before all tests."""
        cls.api = APITestHelper(
            base_url='https://jsonplaceholder.typicode.com',
            default_headers={'Content-Type': 'application/json'}
        )
    
    def test_get_all_posts(self):
        """Test retrieving all posts."""
        response = self.api.get('/posts')
        self.api.assert_status_code(response, 200)
        
        posts = response.json()
        self.assertIsInstance(posts, list, "Response should be a list")
        self.assertGreater(len(posts), 0, "Should have at least one post")
    
    def test_get_single_post(self):
        """Test retrieving a single post."""
        response = self.api.get('/posts/1')
        self.api.assert_status_code(response, 200)
        self.api.assert_response_contains(response, 'id')
        self.api.assert_response_contains(response, 'title')
        self.api.assert_response_contains(response, 'body')
        self.api.assert_response_value(response, 'id', 1)
    
    def test_get_post_not_found(self):
        """Test retrieving non-existent post."""
        response = self.api.get('/posts/99999')
        self.api.assert_status_code(response, 404)
    
    def test_create_post(self):
        """Test creating a new post."""
        new_post = {
            'title': 'Test Post',
            'body': 'This is a test post created by automation',
            'userId': 1
        }
        response = self.api.post('/posts', json_data=new_post)
        self.api.assert_status_code(response, 201)
        
        created_post = response.json()
        self.assertEqual(created_post['title'], new_post['title'])
        self.assertEqual(created_post['body'], new_post['body'])
        self.assertEqual(created_post['userId'], new_post['userId'])
    
    def test_update_post(self):
        """Test updating an existing post."""
        updated_post = {
            'id': 1,
            'title': 'Updated Test Post',
            'body': 'This post has been updated',
            'userId': 1
        }
        response = self.api.put('/posts/1', json_data=updated_post)
        self.api.assert_status_code(response, 200)
        
        result = response.json()
        self.assertEqual(result['title'], updated_post['title'])
    
    def test_delete_post(self):
        """Test deleting a post."""
        response = self.api.delete('/posts/1')
        self.api.assert_status_code(response, 200)
    
    def test_get_user_posts(self):
        """Test retrieving posts for a specific user."""
        response = self.api.get('/posts', params={'userId': 1})
        self.api.assert_status_code(response, 200)
        
        posts = response.json()
        self.assertIsInstance(posts, list)
        # Verify all posts belong to user 1
        for post in posts:
            self.assertEqual(post['userId'], 1)


class TestJSONPlaceholderUsers(unittest.TestCase):
    """Test cases for user endpoints."""
    
    @classmethod
    def setUpClass(cls):
        """Set up test class - runs once before all tests."""
        cls.api = APITestHelper(
            base_url='https://jsonplaceholder.typicode.com',
            default_headers={'Content-Type': 'application/json'}
        )
    
    def test_get_all_users(self):
        """Test retrieving all users."""
        response = self.api.get('/users')
        self.api.assert_status_code(response, 200)
        
        users = response.json()
        self.assertIsInstance(users, list)
        self.assertGreater(len(users), 0)
    
    def test_get_single_user(self):
        """Test retrieving a single user."""
        response = self.api.get('/users/1')
        self.api.assert_status_code(response, 200)
        
        user = response.json()
        self.api.assert_response_contains(response, 'id')
        self.api.assert_response_contains(response, 'name')
        self.api.assert_response_contains(response, 'email')
        self.assertEqual(user['id'], 1)


if __name__ == '__main__':
    unittest.main()

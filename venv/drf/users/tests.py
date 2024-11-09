from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
# Create your tests here.

class UserRegistrationTests(APITestCase):
    def test_user_registration(self):
        url = reverse('register')
        data = {
            "email": "test@example.com",
            "password": "StrongPass@123",
            "name": "Test User"
        }
        response = self.client.post(url, data, format='json')
        
        # Check for success status
        self.assertEqual(response.status_code, 201)
        
        # Check for 'message' instead of 'email'
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'User created successfully')


# test  for user login 
from django.contrib.auth import get_user_model
from .models import CustomUser
from unittest.mock import patch

class LoginViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = CustomUser.objects.create_user(
            email='testuser@example.com',
            password='password123'
        )
        self.url = reverse('login')  # Ensure this matches your URL configuration for the login view

    def test_successful_login(self):
        # Define the login data
        data = {
            "email": "testuser@example.com",
            "password": "password123",
        }
        
        # Make a POST request to the login endpoint
        response = self.client.post(self.url, data, format='json')
        
        # Check that the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that the response contains both access and refresh tokens
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_unsuccessful_login_invalid_email(self):
        # Define incorrect login data
        data = {
            "email": "wronguser@example.com",
            "password": "password123",
        }
        
        # Make a POST request to the login endpoint
        response = self.client.post(self.url, data, format='json')
        
        # Check that the response status is 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Check for the appropriate error message in the response
        self.assertIn('non_field_errors', response.data)

    def test_unsuccessful_login_invalid_password(self):
        # Define login data with an incorrect password
        data = {
            "email": "testuser@example.com",
            "password": "wrongpassword",
        }
        
        # Make a POST request to the login endpoint
        response = self.client.post(self.url, data, format='json')
        
        # Check that the response status is 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Check for the appropriate error message in the response
        self.assertIn('non_field_errors', response.data)
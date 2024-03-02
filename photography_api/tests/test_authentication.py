from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class AuthenticationTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Photographys-list')
        self.user = User.objects.create_user(username='c3po', password='St4rW4r$')
    
    def test_authentication_user(self):
        user = authenticate(username='c3po', password='St4rW4r$')
        self.assertTrue((user is not None), user.is_authenticated)

    def test_get_authentication_user(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_no_authentication_user(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authentication_invalid_username(self):
        user = authenticate(username='username', password='St4rW4r$')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_authentication_invalid_password(self):
        user = authenticate(username='c3po', password='password')
        self.assertFalse((user is not None) and user.is_authenticated)
        
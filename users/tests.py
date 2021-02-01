from .forms import SimpleSignupForm
from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
import json
from datetime import datetime
from django.middleware import csrf
CustomUser = get_user_model()


class UsersTests(TestCase):
    def setUp(self):
        self.signup_data = {
            'username': 'shaker',
            'email': 'shake@gmail.com',
            'user_type': 'CHIEF',
            'password1': 'sucess2016',
            'password2': 'sucess2016'
        }

    def test_signup(self):
        response = self.client.post(
            reverse('account_signup'), data=self.signup_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CustomUser.objects.all().count(), 1)

from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import User

from django.test import TestCase
from .models import User

class UserModelTest(TestCase):
    def test_user_creation(self):
        # Create a User instance
        user = User.objects.create(username='testuser', password='testpassword')

        # Assert that the User was created successfully
        self.assertEqual(User.objects.count(), 1)
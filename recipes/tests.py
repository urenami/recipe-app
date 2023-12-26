from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Recipe

from django.test import TestCase
from users.models import User
from .models import Recipe

class RecipeModelTest(TestCase):
    def test_recipe_creation(self):
        # Create a User instance first
        user = User.objects.create(username='testuser', password='testpassword')

        # Use the created user when creating a Recipe
        recipe = Recipe.objects.create(
            user=user,
            name='Test Recipe',
            cooking_time=30,
            ingredients='Test ingredient 1, Test ingredient 2',
            difficulty='Easy',
            description='This is a test recipe.'
        )

        # Assert that the Recipe was created successfully
        self.assertEqual(Recipe.objects.count(), 1)
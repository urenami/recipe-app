from django.test import TestCase
from .models import Recipe
from .forms import RecipeSearchForm


class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Recipe.objects.create(
            name="Spaghetti Bolognese",
            cooking_time=10,
            difficulty="Easy",
            ingredients="Spaghetti, Ground beef, Tomato sauce, Onion, Garlic, Salt, Black pepper",
        )

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_recipe_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field("name").max_length
        self.assertEqual(max_length, 120)

    def test_cooking_time(self):
        recipe = Recipe.objects.get(id=1)
        cooking_time = recipe.cooking_time
        self.assertEqual(cooking_time, 10)

    def test_ingredients_list(self):
        recipe = Recipe.objects.get(id=1)
        ingredients = recipe.ingredients
        self.assertEqual(
            ingredients,
            "Spaghetti, Ground beef, Tomato sauce, Onion, Garlic, Salt, Black pepper",
        )

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), "/list/1")

    def test_difficulty_calculation(self):
        recipe = Recipe.objects.get(id=1)
        print("Cooking Time:", recipe.cooking_time)
        print("Ingredients Length:", len(recipe.ingredients.split(", ")))
        print(recipe.calculate_difficulty())
        self.assertEqual(recipe.calculate_difficulty(), "Easy")


class RecipesSearchFormTest(TestCase):

    def test_form_renders_recipe_diff_input(self):
        form = RecipeSearchForm()
        self.assertIn("recipe_diff", form.as_p())

    def test_form_renders_chart_type_input(self):
        form = RecipeSearchForm()
        self.assertIn("chart_type", form.as_p())

    def test_form_valid_data(self):
        form = RecipeSearchForm(data={"recipe_diff": "#1", "chart_type": "#2"})
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = RecipeSearchForm(data={"recipe_diff": "", "chart_type": ""})
        self.assertFalse(form.is_valid())

from django.db import models
from django.shortcuts import reverse

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.FloatField(help_text='in minutes')
    difficulty = models.CharField(max_length=50, default='unknown')
    ingredients = models.TextField()
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def __str__(self):
        return str(self.name)

    def calculate_difficulty(self):
        ingredients = self.ingredients.split(', ')
        if self.difficulty == 'Easy':
            return 'Easy'
        elif self.difficulty == 'Intermediate':
            return 'Intermediate'
        elif self.difficulty == 'Hard':
            return 'Hard'
        else:
           
            if self.cooking_time < 20 and len(ingredients) < 7:
                return 'Easy'
            elif self.cooking_time >= 20 and len(ingredients) < 7:
                return 'Intermediate'
            elif self.cooking_time >= 20 and len(ingredients) >= 7:
                return 'Hard'
            else:
                return 'Unknown'

    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})

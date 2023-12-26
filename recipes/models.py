from django.db import models

# Create your models here.
from django.db import models
from users.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    cooking_time = models.IntegerField()  # Assuming cooking time is in minutes
    ingredients = models.TextField()
    difficulty = models.CharField(max_length=50)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

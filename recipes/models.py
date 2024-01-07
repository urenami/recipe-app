from django.db import models
from django.shortcuts import reverse

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    cooking_time = models.IntegerField()  
    ingredients = models.TextField()
    difficulty = models.CharField(max_length=50)
    description = models.TextField()
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
       return reverse ('recipes:detail', kwargs={'pk': self.pk})
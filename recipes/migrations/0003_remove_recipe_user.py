# Generated by Django 4.2.8 on 2024-01-06 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='user',
        ),
    ]
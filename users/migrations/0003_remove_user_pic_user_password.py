# Generated by Django 4.2.8 on 2024-01-07 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_password_user_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pic',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]

from django.db import models

class User(models.Model):
    user_id = models.IntegerField(primary_key=True, unique=True)
    user_name = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=40)
    profile_picture = models.ImageField(blank=True)
# Create your models here.

# UNIQUE KEY `user_id_UNIQUE` (`user_id`)
# Unique key needed?

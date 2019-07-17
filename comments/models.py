from django.db import models

class Comments(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    text = models.TextField()
    likes = models.IntegerField(blank=True)
    dislikes = models.IntegerField(blank=True)
# What kind of relationship? many-to-many? many-to-one? one-to-one?

# Create your models here.

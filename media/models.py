from django.db import models

class Media(models.Model):
    media_id = models.IntegerField(primary_key=True)
    media = models.ImageField(blank=True)
# Is this a many-to-many relationship? for users/profile_picture & post/media?

# Create your models here.

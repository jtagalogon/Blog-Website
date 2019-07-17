from django.db import models

class Blog(models.Model):
    blog_id = models.IntegerField(primary_key=True)
    blog_name = models.CharField(max_length=100)
    blog_text = models.TextField()
    blogger = models.ForeignKey(Users, on_delete=models.CASCADE)
    # Does it matter where this foreign key goes?
    
# Create your models here.

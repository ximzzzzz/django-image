from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField()
    content = models.TextField()
    
    def __str__(self):
        return self.content
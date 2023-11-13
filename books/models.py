from django.db import models
from django.contrib.auth.models import User

# Models
    
class Books(models.Model):

    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=100)
    author      = models.CharField(max_length=100)
    editorial   = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    used        = models.BooleanField(default=True)
    price       = models.CharField(max_length=20)
    register    = models.DateTimeField(auto_now_add=True)
    quantity    = models.IntegerField()
    image_url   = models.CharField(max_length=300, blank=False)

    def __str__(self):
        return self.name + '-' + self.editorial

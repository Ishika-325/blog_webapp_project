from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content=models.TextField()
    created_on=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=100, default='select')
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} created on {self.created_on}"

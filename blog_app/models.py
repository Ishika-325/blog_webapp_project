from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    CATEGORIES = [
        ('Technology', 'Technology'),
        ('Lifestyle', 'Lifestyle'),
        ('Education', 'Education'),
        ('Health & Wellness', 'Health & Wellness'),
        ('Business & Finance', 'Business & Finance'),
        ('Travel & Culture', 'Travel & Culture'),
        ('Entertainment', 'Entertainment'),
        ('Personal Growth', 'Personal Growth'),
    ]


    title = models.CharField(max_length=100)
    content=models.TextField()
    created_on=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=100)

    
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} created on {self.created_on}"

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateField(auto_now=True)
    
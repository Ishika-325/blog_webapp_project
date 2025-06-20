from .models import Blog
from django import forms 

class BlogForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'content', 'category']
        model = Blog


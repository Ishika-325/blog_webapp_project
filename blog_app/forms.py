from .models import Blog
from django import forms 
from .models import Comment

class BlogForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'content', 'category']
        model = Blog

class CommentForm(forms.ModelForm):
    class Meta:
        fields = ['content']
        model = Comment
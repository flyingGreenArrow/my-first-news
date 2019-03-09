from django import forms 
from .models import Post, User_sys


class Post_Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


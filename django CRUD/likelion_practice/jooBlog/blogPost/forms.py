from django import forms
from .models import Post

class PostUpdate(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body']
from django.forms import ModelForm
from .models import Post
from django import forms

class NewsForm(ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'postType', 'postCategory', 'title', 'text']
        widgets = {
            'author': forms.Select(attrs={
                'class': 'form-control'
            }),
            'postType': forms.Select(attrs={
                'class': 'form-control'
            }),
            'postCategory': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title of post'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write you text in here'
            }),
        }
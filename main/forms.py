from django import forms

from .models import *


class BlogForm(forms.ModelForm):
    title = forms.CharField(
    label= "Blog post title", 
    max_length= 100,
    widget=forms.TextInput(attrs={
        'placeholder': 'Enter the title of your blog post'
    })
    )
    
    mission = forms.CharField(
    label= "Mission",
    widget=forms.TextInput(attrs={
        'placeholder': 'Write your mission here...'
    })
    )
    
    vision = forms.CharField(
    label= "Vision",
    widget=forms.TextInput(attrs={
        'placeholder': 'Write your vision here...'
    })
    )
    
    description = forms.CharField(
    label= "Description",
    widget=forms.TextInput(attrs={
        'placeholder': 'Description/ Bio...'
    })
    )
    
    
    class Meta:
        model = AboutUs
        fields = ['title', 'mission', 'vision', 'description']
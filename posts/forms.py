from django import forms

from .models import *


class BlogForm(forms.ModelForm):
    headline = forms.CharField(
    label= "Blog post headline", 
    max_length= 100,
    widget=forms.TextInput(attrs={
        'placeholder': 'Enter the headline of your blog post'
    })
    )
    
    content = forms.CharField(
    label= "content",
    widget=forms.Textarea(attrs={
        'placeholder': 'Write your content here...',
        'rows': 5
    })
    )
    
    reporter = forms.CharField(
    label= "Reporter's name",
    widget=forms.TextInput(attrs={
        'placeholder': 'Reporter...'
    })
    )
    
    category = forms.CharField(
    label= "Category",
    widget=forms.TextInput(attrs={
        'placeholder': 'Category...'
    })
    )
    # reporter = forms.ModelChoiceField(
    # queryset=Reporter.objects.all(),
    # label="Reporter"
    # )

    # category = forms.ModelChoiceField(
    #     queryset=Categories.objects.all(),
    #     label="Category"
    # )
    
    
    class Meta:
        model = Articles
        fields = ['headline', 'content', 'reporter', 'category']
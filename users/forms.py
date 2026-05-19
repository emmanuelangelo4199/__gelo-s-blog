from django import forms
from django.contrib.auth.models import User


class User_update_forms(forms.ModelForm):
    first_name = forms.CharField(
    label= "First Name:", 
    max_length= 50,
    required=False,
    widget=forms.TextInput(attrs={
        'placeholder': 'Enter first name'
    })
    )

    last_name = forms.CharField(
    label= "Last Name:", 
    max_length= 50,
    required=False,
    widget=forms.TextInput(attrs={
        'placeholder': 'Enter last name'
    })
    )

    username = forms.CharField(
    label= "Username:", 
    max_length= 50,
    widget=forms.TextInput(attrs={
        'placeholder': 'Enter  username'
    })
    )

    image = forms.ImageField(
        label = "Upload an image",
        required = False,
        widget = forms.ClearableFileInput()
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'image']

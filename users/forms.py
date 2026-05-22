from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email



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

    email = forms.EmailField(
        label= "Email",
        max_length= 100,
        required= True,
        widget=forms.TextInput(attrs={
        'placeholder': 'Enter  email'
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
        fields = ['first_name', 'last_name', 'email', 'username', 'image']

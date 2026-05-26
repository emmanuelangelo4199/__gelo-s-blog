from django import forms
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm as AuthPasswordResetForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template import loader

from .models import Email


class PasswordResetForm(AuthPasswordResetForm):
    """Surface SMTP errors in DEBUG; production keeps Django's silent failure."""

    def send_mail(
        self,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name=None,
    ):
        if not settings.DEBUG:
            return super().send_mail(
                subject_template_name,
                email_template_name,
                context,
                from_email,
                to_email,
                html_email_template_name=html_email_template_name,
            )

        subject = loader.render_to_string(subject_template_name, context)
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)
        from_email = from_email or settings.DEFAULT_FROM_EMAIL
        message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        if html_email_template_name is not None:
            html_body = loader.render_to_string(html_email_template_name, context)
            message.attach_alternative(html_body, 'text/html')
        message.send(fail_silently=False)




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
        label="First Name:",
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter first name'})
    )

    last_name = forms.CharField(
        label="Last Name:",
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter last name'})
    )

    username = forms.CharField(
        label="Username:",
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter username'})
    )

    email = forms.EmailField(
        label="Email:",
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter email'})
    )

    image = forms.ImageField(
        label="Upload an image",
        required=False,
        widget=forms.ClearableFileInput()
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'image']

class EmailForms(forms.ModelForm):
    email = forms.EmailField(
        label= "Email:",
        required= True
    )

    class Meta:
        model = Email
        exclude = ['created_at', 'edited_at', 'message', 'subject']
from django.urls import path
from django.contrib.auth import views as auth_views

from .forms import PasswordResetForm
from .views import *

urlpatterns = [
    path('signup', signup, name='signup'),
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logoutc', logoutc, name='logoutc'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('userbio', user_bio, name='userbio'),
    path('password_reset',
        auth_views.PasswordResetView.as_view(
            template_name='users/password_reset.html',
            form_class=PasswordResetForm,
            email_template_name='registration/password_reset_email.html',
            subject_template_name='registration/password_reset_subject.txt',
        ),
        name='password_reset',
    ),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]

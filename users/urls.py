from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', signup, name='signup'),
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logoutc', logoutc, name='logoutc'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]

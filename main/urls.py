from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blogPost, name='blog'),
    path('create', views.create_P, name='create'),
]

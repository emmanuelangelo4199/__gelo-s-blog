from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blogPost, name='blog'),
    path('create', views.create_P, name='create'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('details/<int:pk>', views.details, name='details'),
]

from django.shortcuts import render, redirect
from django.contrib import admin

from .forms import *
from .models import *

# Create your views here.

def index(request):
    title = "this is my title"
    context = {'title': title}
    return render(request, 'main/index.html', context)

def blogPost(request):
    context = {}
    return render(request, 'main/blog.html', context)

def create_P(request):
    form = BlogForm()
    
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            mission = form.cleaned_data['mission'] 
            vision = form.cleaned_data['vision']
            description = form.cleaned_data['description']

        blog = AboutUs(
            title = title, 
            mission = mission,
            vision = vision,
            description = description
        )
        blog.save()
        return redirect('blog')
    
    context = {'form': form}
    return render(request, 'main/create.html', context)
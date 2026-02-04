from django.shortcuts import render
from django.contrib import admin

# Create your views here.

def index(request):
    title = "this is my title"
    context = {'title': title}
    return render(request, 'main/index.html', context)

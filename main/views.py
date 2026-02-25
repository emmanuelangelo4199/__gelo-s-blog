from django.shortcuts import render, redirect
from django.contrib import admin

from django.views.decorators.csrf import csrf_protect

# Create your views here.

def main(request):
    text = "hello"
    context = {
        text : 'text'
    }
    
    return render(request, "main/subpage.html", context)
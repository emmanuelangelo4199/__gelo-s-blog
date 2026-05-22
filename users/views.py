from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

from .forms import *

def signup(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form':form}
    return render(request, 'users/signup.html', context)

def logoutc(request):

    context = {}
    return render(request, 'users/logoutc.html', context)

def user_bio(request):
    form = User_update_forms(instance=request.user)

    if request.method == 'POST':
        form = User_update_forms(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    context = {'form': form}
    return render(request, 'users/userbio.html', context)
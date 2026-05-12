from django.shortcuts import render

def signup(request):

    context = {}
    return render(request, 'users/signup.html', context)

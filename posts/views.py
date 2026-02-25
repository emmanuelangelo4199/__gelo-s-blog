from django.shortcuts import render, redirect

from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def index(request):
    # fetches all the rows from the BlogPost models 
    blogsP = Articles.objects.all()
    
    
    context = {
        'blogsP': blogsP
    }
    return render(request, 'posts/index.html', context)

def blogPost(request):
    context = {}
    return render(request, 'posts/blog.html', context)

@csrf_protect
def create_P(request):
    form = BlogForm()
    
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            headline = form.cleaned_data['headline']
            content = form.cleaned_data['content'] 
            reporter = form.cleaned_data['reporter']
            category = form.cleaned_data['category']
            
            blog = Articles(
                headline = headline, 
                content = content,
                reporter = reporter,
                category = category,
            )
            blog.save()
            return redirect('index')
    
    context = {'form': form}
    return render(request, 'posts/create.html', context)
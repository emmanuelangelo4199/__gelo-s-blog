from django.shortcuts import render, redirect

from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def index(request):
    # fetches all the rows from the BlogPost models 
    blogsP = Articles.objects.all()
    
    # if there isn't any data in the blog post section
    blogscount = blogsP.count()
    
    
    context = {
        'blogsP': blogsP,
        'blogscount': blogscount
    }
    return render(request, 'posts/index.html', context)

def blogPost(request):
    context = {}
    return render(request, 'posts/blog.html', context)

@csrf_protect
def create_P(request):
    # this form is for the create template {{form|crispy}} the one created for forms..
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

def edit (request, pk):
    # this gets the message from directly from the Article model/ database
    blog = Articles.objects.get(id=pk)
    
    form = BlogForm(instance=blog)
    
    # this tell that someone is trying to populate data in the database
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog.save()
            return redirect('index')
    
    context = {'form': form}
    return render(request, 'posts/edit.html', context)
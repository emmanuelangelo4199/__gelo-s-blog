from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

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

@login_required
def blogPost(request):
    # shows all blogs created by different users
    # blogsP = Articles.objects.all().order_by('')


    blogsP = Articles.objects.filter(reporter=request.user)
    blogscount = blogsP.count()
    
    context = {
        'blogsP': blogsP,
        'blogscount': blogscount
    }
    return render(request, 'posts/blog.html', context)

@csrf_protect
@login_required
def create_P(request):
    # this form is for the create template {{form|crispy}} the one created for forms..
    form = BlogForm()
    
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            headline = form.cleaned_data['headline']
            content = form.cleaned_data['content'] 
            reporter = form.cleaned_data['reporter']
            category = form.cleaned_data['category']
            image = form.cleaned_data['image']
            tags = form.cleaned_data['tags']
            
            blog = Articles(
                headline = headline, 
                content = content,
                reporter = reporter,
                category = category,
                featured_Image = image,
            )
            blog.save()
            blog.tags.set(tags)
            
            return redirect('index')
    
    context = {'form': form}
    return render(request, 'posts/create.html', context)

@login_required
def edit (request, pk):
    # this gets the message from directly from the Article model/ database
    blog = Articles.objects.get(id=pk)

    if request.user != blog.reporter:
        return redirect('index')
    
    form = BlogForm(instance=blog)
    
    # this tell that someone is trying to populate data in the database
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    context = {'form': form}
    return render(request, 'posts/edit.html', context)

@login_required
def delete (request, id):
    # Retrieve the object or raise a 404 error if it doesn't exist
    blog = Articles.objects.get(id=id)

    if request.user != blog.reporter:
        return redirect('index')
    
    if request.method == "POST":
        # If the request is POST, delete the object
        blog.delete()
        return redirect('index')
    
    # If it's a not POST a GET request to show the confirmation page 
    # render a template asking for confirmation
    context = {'blog': blog}
    return render(request, 'posts/delete.html', context)

def details(request, pk):
    blog = Articles.objects.get(id=pk)



    context = {'blog': blog}
    return render(request, 'posts/details.html', context)
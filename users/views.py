from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .forms import EmailForms
from .forms import User_update_forms
from .forms import CustomUserCreationForm
from .models import Email
from django.views.generic import FormView, ListView
from django.core.mail import send_mail

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



class BasicEmailView(FormView, ListView):
    template_name = "password_reset.html"
    context_object_name = 'mydata'
    model = Email
    form_class = EmailForms
    success_url = '/'

    def form_valid(self, form):

        my_subject = "Email from Django app"
        my_message = "Message from the app"
        my_recipient = form.cleaned_data['email']

        send_mail(
            subject= my_subject,
            message= my_message,
            recipient_list= [my_recipient],
            from_email= None,
            fail_silently=False,
        )

        obj = Email(
            subject= my_subject,
            message= my_message,
            email= my_recipient, 
        )

        obj.save()

        return super().form_valid(form)

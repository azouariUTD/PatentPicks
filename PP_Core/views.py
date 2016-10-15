from django.shortcuts import render
from django.utils import timezone
from .models import Invention, Category, User
from .forms import RegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

# Create your views here.
def home(request):
    inventions = Invention.objects.all()
    return render(request, 'PP_Core/home.html', {'inventions':inventions})

def discover(request):
    categories = Category.objects.all()
    return render(request, 'PP_Core/discover.html', {"categories":categories})

def howitworks(request):
    title_from_view = "How it Works"
    return render(request, 'PP_Core/howitworks.html', {"title_from_view":title_from_view})

def aboutus(request):
    title_from_view = "About us"
    return render(request, 'PP_Core/aboutus.html', {"title_from_view":title_from_view})

#def register(request):
#    title_from_view = "Registration Page"
#    return render(request, 'PP_Core/register.html', {"title_from_view":title_from_view})

def register(request):
    # if this is a POST request we need to process the form data
    title_from_view = "Registration Page"
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            first_name_Val= form.cleaned_data.get('first_name')
            last_name_Val = form.cleaned_data.get('last_name')
            email_Val = form.cleaned_data.get('email')
            password_Val = form.cleaned_data.get('password')


            try:
                User.objects.create(
                    first_name = first_name_Val,
                    last_name = last_name_Val,
                    email = email_Val,
                    password = password_Val,
                    username = email_Val

                )
            except ValueError:
                print(ValueError)
            return HttpResponseRedirect('/login/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'PP_Core/register.html', {'form': form, "title_from_view":title_from_view})

def login_view(request):
    title_from_view = "Login"
    return render(request, 'PP_Core/login.html', {"title_from_view":title_from_view})




from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Invention, Category, User
from PP_Dashboard.models import Profile
from .forms import RegisterForm, UserLoginForm
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
    person = Profile()
    return render(request, 'PP_Core/home.html', {'inventions':inventions,'person':person})

def discover(request):
    categories = Category.objects.all()
    categoryNames = []
    categoryAmounts = []
    for i in categories:
        categoryNames.append(i.category_name)
        categoryAmounts.append(i.quantity)
    return render(request, 'PP_Core/discover.html', {"categoryAmounts":categoryAmounts,  "categoryNames":categoryNames})

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


    form = UserLoginForm(request.POST or None)
    #print(request.user)
    #print(request.user.is_authenticated)

    if form.is_valid():
        #print("Form is valid")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect ('home')


    return render(request, 'PP_Core/login.html', {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')


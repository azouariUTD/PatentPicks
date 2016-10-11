from django.shortcuts import render
from django.utils import timezone
from .models import Invention, Category

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

def login(request):
    title_from_view = "Login"
    return render(request, 'PP_Core/login.html', {"title_from_view":title_from_view})

def register(request):
    title_from_view = "Registration Page"
    return render(request, 'PP_Core/register.html', {"title_from_view":title_from_view})






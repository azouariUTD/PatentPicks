from django.shortcuts import render
from django.utils import timezone
from .models import Invention

# Create your views here.
def post_list(request):
    inventions = Invention.objects.all()
    #setlength = inventions.count()
    #numCategories is for front end testing
    return render(request, 'PP_Core/category.html', {'inventions':inventions}, {'numCategories' : range(7) })



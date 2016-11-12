from django.shortcuts import render, redirect
from PP_Core.models import Inventor, Category
from PP_Inventions.forms import InventionForm
from django.views import generic


def add_invention(request):
    if request.method == 'POST':
        form = InventionForm(request.POST, request.FILES)
        if form.is_valid():
            invention = form.save(commit=False)
            invention.inventor = Inventor.objects.get(user_id=request.user)
            invention.save()
            return redirect('add_invention')
    else:
        form = InventionForm()

    return render(request, 'PP_Inventions/add_invention.html', {'form': form})

def start_invention(request):
    categories = Category.objects.all()
    categoryNames = []
    categoryAmounts = []
    for i in categories:
        categoryNames.append(i.category_name)
        categoryAmounts.append(i.quantity)
    return render(request, 'PP_Inventions/start_invention.html', {"categoryAmounts":categoryAmounts,  "categoryNames":categoryNames})

def get_started(request):
    categories = Category.objects.all()
    categoryNames = []
    categoryAmounts = []
    for i in categories:
        categoryNames.append(i.category_name)
        categoryAmounts.append(i.quantity)
    return render(request, 'PP_Inventions/get_started.html',  {"categoryAmounts":categoryAmounts,  "categoryNames":categoryNames})


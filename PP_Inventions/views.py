from django.shortcuts import render, redirect
from PP_Core.models import Inventor, Invention
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


def InventionDetails(request):
    inventionList = Invention.objects.all()
    data = {
        'inventionList': inventionList,
    }

    template = 'PP_Inventions/inventions.html'

    return render(request, template, data)

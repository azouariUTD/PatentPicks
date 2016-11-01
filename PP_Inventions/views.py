from django.shortcuts import render, redirect
from PP_Core.models import Inventor,Invention
from PP_Inventions.forms import InventionForm
from django.views.decorators.http import require_POST

def add_invention(request):
    if request.method == 'POST':
        form = InventionForm(request.POST, request.FILES)
        if form.is_valid():
            invention = form.save(commit=False)
            invention.inventor = Inventor.objects.get(user_id=request.user)
            invention.category_id = form.category.pk
            invention.save()
            return redirect('add_invention')
    else:
        form = InventionForm()

    return render(request, 'PP_Inventions/add_invention.html', {'form': form})
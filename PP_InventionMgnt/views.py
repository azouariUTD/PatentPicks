from django.shortcuts import render, redirect
from PP_Core.models import Inventor,Invention
from PP_InventionMgnt.forms import InventionForm
from django.views.decorators.http import require_POST

"""
def add_invention(request):
    if request.method == 'POST':
        form = InventionForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Invention(Inventor=Inventor.objects.get(user_id=request.user),
                                 category=form.category.pk,
                                 invention_name=form.invention_name,
                                 description=form.description,
                                 video=form.video,
                                 price=form.price,
                                 picture=request.FILES['picture'])
            instance.save()
            return redirect('add_invention')
    else:
        form = InventionForm()

    return render(request,'PP_InventionMgnt/add_invention.html', {'form': form})


"""
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

    return render(request, 'PP_InventionMgnt/add_invention.html', {'form': form})








"""
def add_invention(request):
    if request.method == 'POST':
        form = InventionForm(request.POST)
        if form.is_valid():
            category_val = form.cleaned_data.get('categories')
            inventor_val = form.cleaned_data.get('inventor')
            invention_title_val = form.cleaned_data.get('invention_title')
            invention_description_val = form.cleaned_data.get('invention_description')
            invention_image_val = form.cleaned_data.get('invention_image ')
            invention_video_val = form.cleaned_data.get('invention_video')
            invention_price_val = form.cleaned_data.get('invention_price')



            try:
                Invention.objects.create(
                    category_id=category_val,
                    inventor_id=inventor_val,
                    invention_name=invention_title_val,
                    description=invention_description_val,
                    picture=invention_image_val,
                    video=invention_video_val,
                    price=invention_price_val
                )
            except Exception:
                print(Exception)
            return redirect('add_invention')

    else:
        form = InventionForm()

    template = 'PP_InventionMgnt/add_invention.html'
    data = {
        'form': form,
    }
    return render(request, template, data)

"""
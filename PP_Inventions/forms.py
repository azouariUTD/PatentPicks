from django import forms
from PP_Core.models import Invention, Category
from django.shortcuts import get_object_or_404


class InventionForm(forms.ModelForm):
    class Meta:
        model = Invention
        fields = ['category', 'invention_name', 'description', 'picture', 'video', 'price' ]

    def clean(self):
        cleaned_data = super(InventionForm, self).clean()

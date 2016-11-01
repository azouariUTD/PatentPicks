from django import forms
from PP_Core.models import Invention, Category
from django.shortcuts import get_object_or_404


class InventionForm(forms.ModelForm):
    class Meta:
        model = Invention
        fields = ['invention_name', 'description', 'picture', 'video', 'price']

    #category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    category = forms.CharField(label="Category", required=True)



    def clean(self):
        cleaned_data = super(InventionForm, self).clean()
        choice = cleaned_data.get('category')
        category = get_object_or_404(Category, category_name=choice)

        self.category=category
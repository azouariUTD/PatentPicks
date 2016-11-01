from django import forms
from PP_Core.models import Invention, Category
from django.shortcuts import get_object_or_404

"""
class InventionForm(forms.Form):
    invention_name = forms.CharField()
    description = forms.CharField()
    picture = forms.ImageField()
    video = forms.URLField()
    price = forms.DecimalField()
    category = forms.CharField(label="Category", required=True)

    def clean(self):
        cleaned_data = super(InventionForm, self).clean()
        choice = cleaned_data.get('category')
        category = get_object_or_404(Category, category_name=choice)
        self.category = category

"""
class InventionForm(forms.ModelForm):
    class Meta:
        model = Invention
        fields = ['invention_name', 'description', 'picture', 'video', 'price']

    #category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    category = forms.CharField(label="Category", required=True)



    def clean(self):
        cleaned_data = super(InventionForm, self).clean()
        choice = cleaned_data.get('category')
        #category = Category.objects.get(category_name=choice)
        category = get_object_or_404(Category, category_name=choice)
        #comment = get_object_or_404(Comment, pk=comment_id)

        self.category=category













"""



class InventionForm(forms.ModelForm):
    class Meta:
        model = Invention
        fields = ['invention_name', 'description',  'price']

    def clean(self):
        cleaned_data = super(InventionForm, self).clean()
        invention_name = cleaned_data.get('invention_name', '')
        description = cleaned_data.get('description', '')
        price = cleaned_data.get('price')

        try:
            Invention.objects.get(
                invention_name__exact=invention_name.strip()
            )
            exists = True
        except Invention.DoesNotExist:
            exists = False

        if exists:
            raise forms.ValidationError("Invention with the same name exists!")


"""
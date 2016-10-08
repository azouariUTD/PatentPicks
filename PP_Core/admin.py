from django.contrib import admin
from .models import Category, Inventor, Invention, InventionDetail

admin.site.register(Category)
admin.site.register(Inventor)
admin.site.register(Invention)
admin.site.register(InventionDetail)

# Register your models here.

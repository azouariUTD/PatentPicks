from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Category, Inventor, Invention, InventionDetail
from PP_Dashboard.models import Profile

class InventionInline(admin.TabularInline):
    model = Invention
    extra = 0
    readonly_fields = ('inventor','category','invention_name','description','video','price',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':35})},
    }


class InventionDetailInline(admin.TabularInline):
    model = InventionDetail
    extra = 0
    readonly_fields = ('user','comments','improve','pledge','isHidden','isSaved',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':35})},
    }


class CategoryAdmin(admin.ModelAdmin):
    inlines = [InventionInline]

class InventorAdmin(admin.ModelAdmin):
    inlines = [InventionInline]

class InventionAdmin(admin.ModelAdmin):
    inlines = [InventionDetailInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Inventor, InventorAdmin)
admin.site.register(Invention, InventionAdmin)
admin.site.register(InventionDetail)

admin.site.register(Profile)

# Register your models here.

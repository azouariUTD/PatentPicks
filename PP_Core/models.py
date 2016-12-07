from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField



# Create your models here.
class Inventor(models.Model):
    user = models.ForeignKey(User)
    bio = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.user.email


class Category(models.Model):
    category_name = models.CharField(max_length=60)
    category_description = models.TextField()
    quantity = models.IntegerField()
    add_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "categories"


class Invention(models.Model):
    inventor = models.ForeignKey(Inventor)
    category = models.ForeignKey(Category)
    invention_name = models.CharField(max_length=250)
    description = models.TextField()
    picture = models.ImageField(upload_to='inventions/%Y/%m/%d/')
    video = models.URLField(max_length=200)
    price = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
    add_date = models.DateTimeField(auto_now_add=True, blank=True)
    slug = AutoSlugField(populate_from='invention_name', unique_with='add_date__day')

    def __str__(self):
        return self.invention_name


class InventionDetail(models.Model):
    user = models.ForeignKey(User)
    invention = models.ForeignKey(Invention)
    pledge = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
    comments = models.TextField()
    improve = models.TextField()
    isHidden = models.BooleanField()
    isSaved = models.BooleanField()
    isViewed = models.BooleanField()
    isPicked = models.BooleanField()
    add_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.user.email + ' ' + self.invention.invention_name

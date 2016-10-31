from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Inventor(models.Model):
    user = models.ForeignKey(User)
    bio = models.TextField()

    def __str__(self):
        return self.user.email


class Category(models.Model):
    category_name = models.CharField(max_length=60)
    category_description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.category_name + " " + str(self.quantity) + " patents."

    class Meta:
        verbose_name_plural = "categories"


class Invention(models.Model):
    inventor = models.ForeignKey(Inventor)
    category = models.ForeignKey(Category)
    invention_name = models.CharField(max_length=250)
    description = models.TextField()
    picture = models.ImageField(upload_to='static/PP_core/', default='static/PP_core/PP_Logo.png')
    video = models.URLField(max_length=200)
    price = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)

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

    def __str__(self):
        return self.user.email + ' ' + self.invention.invention_name

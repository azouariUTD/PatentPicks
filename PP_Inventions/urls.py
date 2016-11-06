from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^inventions', views.InventionDetails, name='InventionDetails'),
    url(r'^add_invention', views.add_invention, name='add_invention'),

]
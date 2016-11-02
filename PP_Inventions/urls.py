from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'', views.add_invention, name='add_invention'),
]
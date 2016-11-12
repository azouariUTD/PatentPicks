from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^start_invention/get_started', views.get_started, name='get_started' ),
    url(r'^start_invention/', views.start_invention, name='start_invention' ),
    url(r'', views.add_invention, name='add_invention'),

]
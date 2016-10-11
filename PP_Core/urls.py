from django.conf.urls import url
from . import views

urlpatterns = [	
    url(r'^discover/', views.discover, name='discover'),
    url(r'^howitworks/', views.howitworks, name ='howitworks'), 
    url(r'^aboutus/', views.aboutus, name='aboutus'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'', views.home, name='home'),
]
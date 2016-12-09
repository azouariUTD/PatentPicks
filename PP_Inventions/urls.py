from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^start_invention/get_started', views.get_started, name='get_started' ),
    url(r'^start_invention/', views.start_invention, name='start_invention' ),
    url(r'^invention_navigation/', views.invention_navigation, name='invention_navigation' ),
    url(r'^basics/', views.basics, name='basics' ),
    url(r'^story/', views.story, name='story' ),
    url(r'^rewards/', views.rewards, name='rewards' ),
    url(r'^material/', views.material, name='material' ),
    url(r'^post_basics/', views.post_basics, name='post_basics' ),
    url(r'^post_story/', views.post_story, name='post_story' ),
    url(r'^post_about_you/', views.post_about_you, name='post_about_you' ),
    url(r'^add_invention', views.add_invention, name='add_invention'),
    url(r'^inventions', views.InventionDetails, name='InventionDetails'),
    url(r'^(?P<slug>[\w-]+)/$', views.invention, name='invention'),
]
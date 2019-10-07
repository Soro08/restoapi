from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('about', views.about, name='about'),
    path('team', views.team, name='team'),
    path('reservation', views.reservation, name='reservation'),
    path('menu', views.menu, name='menu'),
    path('specialite', views.specialite, name='specialite'),
    
]

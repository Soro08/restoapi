from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from .apiviews import PlatViewSet


router = DefaultRouter()
router.register('plataip', PlatViewSet, base_name='plats')

urlpatterns = [
    path('', views.home, name='home'),

    path('about', views.about, name='about'),
    path('team', views.team, name='team'),
    path('reservation', views.reservation, name='reservation'),
    path('menu', views.menu, name='menu'),
    path('specialite', views.specialite, name='specialite'),
    
]
urlpatterns += router.urls
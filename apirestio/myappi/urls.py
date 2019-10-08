from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from .apiviews import PlatViewSet, MenuViewSet, CategorieViewSet, SpecialiteViewSet


router = DefaultRouter()
router.register('apiplat', PlatViewSet, base_name='apiplat')
router.register('apispecialite', SpecialiteViewSet, base_name='apispecialite')
router.register('apicategorie', CategorieViewSet, base_name='apicategorie')
router.register('apimenu', MenuViewSet, base_name='apimenu')

urlpatterns = [
    path('home', views.home, name='home'),

    path('about', views.about, name='about'),
    path('team', views.team, name='team'),
    path('reservation', views.reservation, name='reservation'),
    path('menu', views.menu, name='menu'),
    path('specialite', views.specialite, name='specialite'),
    
]
urlpatterns += router.urls
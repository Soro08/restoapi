from rest_framework import viewsets

from .models import *
from .serializers import PlatSerializer, Categorie, Menu, Specialite


class PlatViewSet(viewsets.ModelViewSet):
    queryset = Plat.objects.all().prefetch_related('categorie')
    serializer_class = PlatSerializer
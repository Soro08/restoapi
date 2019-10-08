import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from django.db.models import Q
from .models import *


class SpecialiteNode(DjangoObjectType):
    class Meta:
        model = Specialite
        filter_fields = ['titre','platspecial']
        interfaces = (relay.Node, )

class CategorieNode(DjangoObjectType):
    class Meta:
        model = Categorie
        filter_fields = ['titre','platcateg']
        interfaces = (relay.Node, )


class MenuNode(DjangoObjectType):
    class Meta:
        model = Menu
        filter_fields = ['jour','statut']
        interfaces = (relay.Node, )

class PlatNode(DjangoObjectType):
    class Meta:
        model = Plat
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
            'specialite': ['exact'],
            'specialite__titre': ['exact'],
        }
        interfaces = (relay.Node, )






class Query(object):
    # specialite = graphene.Field(SpecialiteType,id=graphene.Int(),titre=graphene.String())

    # all_specialites = graphene.List(SpecialiteType, search=graphene.String())
    specialite = relay.Node.Field(SpecialiteNode)
    all_specialites = DjangoFilterConnectionField(SpecialiteNode)

    categorie = relay.Node.Field(CategorieNode)
    all_categories =  DjangoFilterConnectionField(CategorieNode)

    menu = relay.Node.Field(MenuNode)
    all_menus =  DjangoFilterConnectionField(MenuNode)

    plat = relay.Node.Field(PlatNode)
    all_plats =  DjangoFilterConnectionField(PlatNode)

    # def resolve_all_specialites(self, info,search=None, **kwargs):
    #     if search:
    #         return Specialite.objects.filter(titre__icontains = search)
    #     return Specialite.objects.all()

    # def resolve_all_categories(self, info, **kwargs):
    #     return Categorie.objects.all()

    # def resolve_all_menus(self, info, **kwargs):
    #     return Menu.objects.all()

    # def resolve_all_plats(self, info, **kwargs):
    #     # We can easily optimize query count in the resolve method
    #     return Plat.objects.select_related().all()


    # def resolve_specialite(self, info, **kwargs):
    #     id = kwargs.get('id')
    #     titre = kwargs.get('titre')

    #     if id is not None:
    #         return Specialite.objects.get(pk=id)

    #     if titre is not None:
    #         return Specialite.objects.get(titre=titre)

    #     return None


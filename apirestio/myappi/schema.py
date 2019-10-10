import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from django.db.models import Q
from .models import *
from gestion.models import (Acceuil, AcceuilImage,About, Testimonial, Teams, Horraire)
############### Gestion API

class AcceuilNode(DjangoObjectType):
    class Meta:
        model = Acceuil
        filter_fields = ['statut',]
        interfaces = (relay.Node, )

class AcceuilImageNode(DjangoObjectType):
    class Meta:
        model = AcceuilImage
        filter_fields = ['statut',]
        interfaces = (relay.Node, )

class AboutNode(DjangoObjectType):
    class Meta:
        model = About
        filter_fields = ['statut',]
        interfaces = (relay.Node, )

class TestimonialNode(DjangoObjectType):
    class Meta:
        model = Testimonial
        filter_fields = ['statut',]
        interfaces = (relay.Node, )

class TeamsNode(DjangoObjectType):
    class Meta:
        model = Teams
        filter_fields = ['statut',]
        interfaces = (relay.Node, )

class HorraireNode(DjangoObjectType):
    class Meta:
        model = Horraire
        filter_fields = ['statut',]
        interfaces = (relay.Node, )


######################### My API
class SpecialiteNode(DjangoObjectType):
    class Meta:
        model = Specialite
        filter_fields = ['titre','platspecial']
        interfaces = (relay.Node, )

class CategorieNode(DjangoObjectType):
    class Meta:
        model = Categorie
        filter_fields = ['titre','platcateg','statut',]
        interfaces = (relay.Node, )


class MenuNode(DjangoObjectType):
    class Meta:
        model = Menu
        filter_fields = ['jour','statut', 'position']
        interfaces = (relay.Node, )

class PlatNode(DjangoObjectType):
    class Meta:
        model = Plat
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
            'prix': ['lt', 'gt'],
            'specialite': ['exact'],
            'specialite__titre': ['exact'],
            'menu__position': ['exact'],
        }
        interfaces = (relay.Node, )






class Query(object):
## My API
    specialite = relay.Node.Field(SpecialiteNode)
    all_specialites = DjangoFilterConnectionField(SpecialiteNode)

    categorie = relay.Node.Field(CategorieNode)
    all_categories =  DjangoFilterConnectionField(CategorieNode)

    menu = relay.Node.Field(MenuNode)
    all_menus =  DjangoFilterConnectionField(MenuNode)

    plat = relay.Node.Field(PlatNode)
    all_plats =  DjangoFilterConnectionField(PlatNode)

## Gestion

    acceuil = relay.Node.Field(AcceuilNode)
    all_acceuils =  DjangoFilterConnectionField(AcceuilNode)

    imgacceuil = relay.Node.Field(AcceuilImageNode)
    all_imgacceuils =  DjangoFilterConnectionField(AcceuilImageNode)

    about = relay.Node.Field(AboutNode)
    all_abouts =  DjangoFilterConnectionField(AboutNode)

    testimonial = relay.Node.Field(TestimonialNode)
    all_testimonials =  DjangoFilterConnectionField(TestimonialNode)


    all_teams =  DjangoFilterConnectionField(TeamsNode)

    all_horraires =  DjangoFilterConnectionField(HorraireNode)






   
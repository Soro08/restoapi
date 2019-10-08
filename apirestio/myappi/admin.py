from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class SpecialiteAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'statut',
        'date_add',
    )
    search_fields = ('titre',)

class CategorieAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
    )
    
class MenuAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'jour',
        'position',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
    )


class PlatAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'specialite',
        'categorie',
        'titre',
        'prix',
        'ingredient',
        'image_menu',
        'image_special',
        'statut',
    )
    list_filter = (
        'specialite',
        'categorie',
        'statut',
        'date_add',
        'date_upd',
    )
    search_fields = ('titre',)
    #date_hierarchy = ('date_add',)
    filter_horizontal = ('menu',)

def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Specialite, SpecialiteAdmin)
_register(models.Categorie, CategorieAdmin)
_register(models.Menu, MenuAdmin)
_register(models.Plat, PlatAdmin)

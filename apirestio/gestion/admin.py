from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models

class AcceuilImageInLine(admin.TabularInline):
    model = models.AcceuilImage
    extra = 0


class AcceuilAdmin(admin.ModelAdmin):

    list_display = (
        'titre',
        'video_url',
        'logo',
        'statut',
        'date_add',
    )
    list_filter = (
        'statut',
        'date_add',
    )
    #inlines = [AcceuilImageInLine,]


class AcceuilImageAdmin(admin.ModelAdmin):

    list_display = ( 'image', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'statut',
        'date_add',
    )


class AboutAdmin(admin.ModelAdmin):

    list_display = (
        'image',
        'titre',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
    )


class TestimonialAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'role',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
    )


class TeamsAdmin(admin.ModelAdmin):

    list_display = (
        'image',
        'user',
        'role',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'user',
        'statut',
        'date_add',
        'date_upd',
    )


class TeamLienAdmin(admin.ModelAdmin):

    list_display = (
        'icone',
        'url',
        'team',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'team',
        'statut',
        'date_add',
        'date_upd',
        
        'icone',
        'url',
        'team',
        'statut',
        'date_add',
        'date_upd',
    )


class HorraireAdmin(admin.ModelAdmin):

    list_display = (
        
        'jour',
        'heure_debut',
        'heure_fin',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Acceuil, AcceuilAdmin)
_register(models.AcceuilImage, AcceuilImageAdmin)
_register(models.About, AboutAdmin)
_register(models.Testimonial, TestimonialAdmin)
_register(models.Teams, TeamsAdmin)
_register(models.Horraire, HorraireAdmin)

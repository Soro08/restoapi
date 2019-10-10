from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Acceuil(models.Model):
    titre = models.CharField(max_length=255)
    video_url = models.URLField()
    logo = models.ImageField(upload_to='logo')
    
    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

class AcceuilImage(models.Model):
    
    image = models.ImageField(upload_to='home')
    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.url



class About(models.Model):
    image = models.ImageField(upload_to='about')
    titre = models.CharField(max_length=255)
    description = models.TextField()

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

class Testimonial(models.Model):
    message = models.TextField()
    user = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

class Teams(models.Model):
    image = models.ImageField(upload_to='teams')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='temuser')
    role = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)

class TeamLien(models.Model):
    FB = 'fab fa-facebook-f'
    TW = 'fab fa-twitter'
    INST = 'fab fa-instagram'
    GP = 'fab fa-google-plus-g'
    LIST_ICONES = [
        (FB, 'Facebook'),
        (TW, 'Twitter'),
        (INST, 'Instagram'),
        (GP, 'Google Plus')
    ]
    icone = models.CharField(max_length=200, choices=LIST_ICONES, default=FB)
    url = models.URLField()
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='teamliens')

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url


class Horraire(models.Model):
    jour = models.CharField(max_length=255)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.jour
    
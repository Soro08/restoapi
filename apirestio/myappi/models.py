from django.db import models

# Create your models here.
class Specialite(models.Model):
    titre = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

class Categorie(models.Model):
    titre = models.CharField(max_length=255)
    
    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.titre

class Menu(models.Model):
    jour = models.CharField(max_length=255)
    position = models.PositiveIntegerField()

    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.jour

class Plat(models.Model):
    specialite = models.ForeignKey(Specialite, on_delete = models.CASCADE, related_name='platspecial')
    categorie = models.ForeignKey(Categorie, on_delete = models.CASCADE, related_name='platcateg')
    menu = models.ManyToManyField(Menu)
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    ingredient = models.TextField(blank=True)
    prix = models.DecimalField(default=1000,max_digits=10, decimal_places=2)
    image_menu = models.ImageField(upload_to='plat')
    image_special = models.ImageField(upload_to='plat')

    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

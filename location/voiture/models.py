from django.db import models

# Create your models here.

from django.db import  models
from django.contrib.auth.models import AbstractUser


class Ville(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class Type(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Voiture(models.Model):
    matricule = models.CharField(max_length=100, null=True , unique=True)
    modele= models.CharField(max_length=100, null=True)
    marque= models.CharField(max_length=100, null=True)
    prix_jour = models.DecimalField(max_digits=8, decimal_places=2)
    isdisponibilite = models.BooleanField(default=False)
    nombre_siege = models.IntegerField()
    photo = models.ImageField(upload_to='cars/')
    ville = models.ForeignKey(Ville, related_name="villes",on_delete=models.CASCADE)
    type = models.ForeignKey(Type ,related_name="types", on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.matricule , self.modele , self.marque, self.prix_jour,self.isdisponibilite,self.nombre_siege,self.ville, self.type)

class Reservation(models.Model):
    nombre_siege = models.IntegerField()
    voiture = models.OneToOneField(Voiture , on_delete=models.CASCADE)




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
    photo = models.CharField(max_length=None, null=True)
    ville = models.ForeignKey(Ville,on_delete=models.CASCADE)
    type = models.ForeignKey(Type , on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.matricule , self.modele , self.marque, self.prix_jour,self.isdisponibilite,self.nombre_siege,self.ville, self.type)
class Client(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    age = models.IntegerField()
    date_permis = models.DateField()
    ref_permis = models.CharField(max_length=20)

    def __str__(self):
        return '{} {} {} {} {} {} '.format(self.username , self.email , self.password , self.age , self.date_permis ,self.ref_permis)


class Reservation(models.Model):
    date_debut = models.DateField()
    date_fin = models.DateField()
    voiture = models.OneToOneField(Voiture , on_delete=models.CASCADE)
    client = models.ForeignKey(Client , on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {} {}  '.format(self.date_debut , self.date_fin , self.voiture , self.client)


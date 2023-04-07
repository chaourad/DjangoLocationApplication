from rest_framework import serializers
from .models import *




class VilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ville
        fields = '__all__'





class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class VoitureSerializer(serializers.ModelSerializer):
    #date = serializers.DateField(source="nom")
    photo = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Voiture
        fields = ('matricule','modele','marque','prix_jour','isdisponibilite','nombre_siege','photo','ville','type')
class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ('date_debut', 'date_fin','voiture','client')

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'

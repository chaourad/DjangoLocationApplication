from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.decorators import api_view
from  rest_framework import generics
from rest_framework import viewsets


from .serializer import *
from .serializer import *
# Create your views here.

class VilleViewSet(viewsets.ModelViewSet):

    queryset = Ville.objects.all()
    serializer_class = VilleSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ['nom']


class TypeViewSet(viewsets.ModelViewSet):

    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ['nom']


class VoitureViewSet(viewsets.ModelViewSet):

    queryset = Voiture.objects.all()
    serializer_class = VoitureSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ['modele', 'marque', 'prix_jour', 'isdisponibilite', 'nombre_siege', 'ville', 'type']
    search_fields = ['modele']

    def test(self ):
        queryset = VoitureSerializer.object.all()
        return queryset


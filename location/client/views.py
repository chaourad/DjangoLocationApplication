from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from location.client.serializers import UserSerializer


# Create your views here.
class ClientSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)

    def list(self, request):
        user = User.objects.get(pk=request.user)
        user_data = UserSerializer(user).data
        return  Response(user_data)

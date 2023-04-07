from django import forms

from location.voiture.models import Ville


class ClientForm(forms.ModelForm):
    class Meta:
        model = Ville
        fields = ['nom']

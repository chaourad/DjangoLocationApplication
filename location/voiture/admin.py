from django.contrib import admin

from .models import Ville , Type , Voiture


# Register your models here.



@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('nom' , )
    list_filter = ('nom',)

@admin.register(Ville)
class VilleAdmin(admin.ModelAdmin):
    list_display = ('nom' , )

@admin.register(Voiture)
class VoitureAdmin(admin.ModelAdmin):

    list_display = ('matricule', 'modele', 'marque', 'prix_jour', 'isdisponibilite', 'nombre_siege', 'ville', 'type' )
    list_filter = ('modele', 'marque', 'prix_jour', 'isdisponibilite', 'nombre_siege', 'ville', 'type')
    search_fields = ( 'modele',)
   
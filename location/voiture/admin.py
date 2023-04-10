from django.contrib import admin

from .models import Ville, Type, Voiture, Reservation , Client


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
    search_fields = ( 'ville',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("date_debut" , "date_fin" , "voiture","client")
    list_filter = ("date_debut" , "date_fin" , "voiture","client")
    search_fields = ("voiture",)



@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("username" , "email" , "password" , "age", "date_permis", "ref_permis")
    search_fields = ("email",)

from django.contrib import admin
from .models import Vehicule, Appartement

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

@admin.register(Appartement)
class AppartementAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)
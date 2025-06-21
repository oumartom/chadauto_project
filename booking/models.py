from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from django.utils import timezone

class Vehicule(models.Model):
    nom = models.CharField(max_length=100)
    image = models.ImageField(upload_to='vehicules/')
    
    def __str__(self):
        return self.nom
    
    def get_absolute_url(self):
        return reverse('booking:car_detail', args=[str(self.id)])

class Appartement(models.Model):
    nom = models.CharField(max_length=100)
    image = models.ImageField(upload_to='appartements/')
    
    def __str__(self):
        return self.nom
    
    def get_absolute_url(self):
        return reverse('booking:apartment_detail', args=[str(self.id)])
    

from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class Reservation(models.Model):
    nom_client = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    
    # Relations optionnelles avec véhicule et/ou appartement
    vehicule = models.ForeignKey('Vehicule', on_delete=models.CASCADE, null=True, blank=True)
    appartement = models.ForeignKey('Appartement', on_delete=models.CASCADE, null=True, blank=True)
    
    date_debut = models.DateField(validators=[MinValueValidator(timezone.now().date())])
    date_fin = models.DateField(null=True, blank=True)
    message = models.TextField(blank=True)
    date_reservation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Réservation #{self.id} - {self.nom_client}"
    
    def est_reservation_combinee(self):
        return self.vehicule is not None and self.appartement is not None
    
    
# class Reservation(models.Model):
#     nom_client = models.CharField(max_length=100)
#     email = models.EmailField()
#     telephone = models.CharField(max_length=20)
    
#     # Relation avec véhicule ou appartement
#     vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, null=True, blank=True)
#     appartement = models.ForeignKey(Appartement, on_delete=models.CASCADE, null=True, blank=True)
    
#     date_debut = models.DateField(validators=[MinValueValidator(timezone.now().date())])
#     date_fin = models.DateField()
#     date_reservation = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"Réservation #{self.id} - {self.nom_client}"
    
#     def get_type_reservation(self):
#         if self.vehicule and self.appartement:
#             return "Véhicule et Appartement"
#         elif self.vehicule:
#             return "Véhicule"
#         else:
#             return "Appartement"
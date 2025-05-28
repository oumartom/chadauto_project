from django import forms
from .models import Reservation
from django.core.exceptions import ValidationError
from django.utils import timezone
from django import forms
from .models import Reservation, Vehicule, Appartement
from django.core.exceptions import ValidationError
from django.utils import timezone

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['nom_client', 'email', 'telephone', 'vehicule', 'appartement', 'date_debut', 'date_fin', 'message']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vehicule'].queryset = Vehicule.objects.all()
        self.fields['appartement'].queryset = Appartement.objects.all()
        self.fields['vehicule'].required = False
        self.fields['appartement'].required = False
    
    def clean(self):
        cleaned_data = super().clean()
        date_debut = cleaned_data.get('date_debut')
        date_fin = cleaned_data.get('date_fin')
        vehicule = cleaned_data.get('vehicule')
        appartement = cleaned_data.get('appartement')
        
        if not vehicule and not appartement:
            raise ValidationError("Vous devez sélectionner au moins un véhicule ou un appartement")
        
        if date_debut and date_fin:
            if date_debut > date_fin:
                raise ValidationError("La date de fin doit être postérieure à la date de début")
            if date_debut < timezone.now().date():
                raise ValidationError("La date de début ne peut pas être dans le passé")
        
        return cleaned_data


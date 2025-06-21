from django.shortcuts import redirect, render, get_object_or_404
from .models import Vehicule, Appartement
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ReservationForm
from django.core.validators import MinValueValidator
from django.utils import timezone

def car_list(request):
    vehicules = Vehicule.objects.all()
    return render(request, 'booking/car_list.html', {'vehicules': vehicules})

def apartment_list(request):
    appartements = Appartement.objects.all()
    return render(request, 'booking/apartment_list.html', {'appartements': appartements})

def car_detail(request, id):
    vehicule = get_object_or_404(Vehicule, id=id)
    return render(request, 'booking/car_detail.html', {'vehicule': vehicule})

def apartment_detail(request, id):
    appartement = get_object_or_404(Appartement, id=id)
    return render(request, 'booking/apartment_detail.html', {'appartement': appartement})

# def reserve_both(request):
    vehicule_id = request.GET.get('vehicule_id')
    appartement_id = request.GET.get('appartement_id')
    
    try:
        vehicule = Vehicule.objects.get(id=vehicule_id) if vehicule_id else None
        appartement = Appartement.objects.get(id=appartement_id) if appartement_id else None
    except (Vehicule.DoesNotExist, Appartement.DoesNotExist):
        vehicule = None
        appartement = None
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.vehicule = vehicule
            reservation.appartement = appartement
            reservation.save()
            
            # Envoi de l'email
            send_reservation_email(reservation)
            
            messages.success(request, "Votre réservation a été enregistrée avec succès!")
            return redirect('core:home')
    else:
        form = ReservationForm()
    
    context = {
        'form': form,
        'vehicule': vehicule,
        'appartement': appartement,
    }
    return render(request, 'booking/reserve_both.html', context)

def reserve_both(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            send_reservation_email(reservation)
            messages.success(request, "Your reservation has been successfully completed. A team member will contact you shortly!")
            return redirect('core:home')
    else:
        # Pré-remplir depuis les paramètres GET si disponibles
        initial_data = {}
        if 'vehicule_id' in request.GET:
            initial_data['vehicule'] = request.GET['vehicule_id']
        if 'appartement_id' in request.GET:
            initial_data['appartement'] = request.GET['appartement_id']
        
        form = ReservationForm(initial=initial_data)
    
    return render(request, 'booking/reserve_both.html', {'form': form})

def send_reservation_email(reservation):
    subject = f"Nouvelle réservation #{reservation.id}"
    
    # Construire le message en fonction du type de réservation
    if reservation.est_reservation_combinee():
        reservation_type = "COMBINÉE (Véhicule + Appartement)"
    elif reservation.vehicule:
        reservation_type = "VÉHICULE"
    else:
        reservation_type = "APPARTEMENT"
    
    message = f"""
    NOUVELLE RÉSERVATION ({reservation_type})
    =====================================
    
    Client: {reservation.nom_client}
    Email: {reservation.email}
    Téléphone: {reservation.telephone}
    
    Période: du {reservation.date_debut} au {reservation.date_fin}
    
    Détails:
    """
    
    if reservation.vehicule:
        message += f"\n- Véhicule: {reservation.vehicule.nom}"
    
    if reservation.appartement:
        message += f"\n- Appartement: {reservation.appartement.nom}"
    
    message += f"""
    
    Message client:
    {reservation.message}
    
    =====================================
    Cet email a été envoyé automatiquement depuis le système de réservation.
    """
    
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        ['chadauto.housing@gmail.com'],  # Email du destinataire
        fail_silently=False,
    )

def send_combined_reservation_email(reservation):
    subject = f"Nouvelle réservation combinée #{reservation.id}"
    
    message = f"""
    Nouvelle réservation combinée reçue :

    Client: {reservation.nom_client}
    Email: {reservation.email}
    Téléphone: {reservation.telephone}

    Véhicule réservé: {reservation.vehicule.nom}
    Appartement réservé: {reservation.appartement.nom}

    Période: du {reservation.date_debut} au {reservation.date_fin}

    Message supplémentaire:
    {reservation.message}

    ---
    Cet email a été envoyé automatiquement depuis le système de réservation.
    """
    
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        ['chadauto.housing@gmail.com'],  # Email de destination
        fail_silently=False,
    )
# def send_reservation_email(reservation):
    subject = f"Confirmation de réservation #{reservation.id}"
    
    message = f"""
    Bonjour {reservation.nom_client},
    
    Merci pour votre réservation chez ChadAuto&House Rental.
    
    Détails de la réservation:
    - Type: {reservation.get_type_reservation()}
    - Date début: {reservation.date_debut}
    - Date fin: {reservation.date_fin}
    - Téléphone: {reservation.telephone}
    
    Nous vous contacterons bientôt pour confirmation.
    
    Cordialement,
    L'équipe ChadAuto&House Rental
    """
    
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [reservation.email],
        fail_silently=False,
    )
    
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class CombinedReservation(models.Model):
    nom_client = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    
    vehicule = models.ForeignKey('Vehicule', on_delete=models.CASCADE)
    appartement = models.ForeignKey('Appartement', on_delete=models.CASCADE)
    
    date_debut = models.DateField(validators=[MinValueValidator(timezone.now().date())])
    date_fin = models.DateField()
    message = models.TextField(blank=True)
    date_reservation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Réservation combinée #{self.id} - {self.nom_client}"
from django.shortcuts import render
from booking.models import Vehicule, Appartement
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')
    

def services(request):
    service_type = request.GET.get('type', 'all')
    
    # Récupération des éléments selon le type
    if service_type == 'car':
        vehicules = Vehicule.objects.all()
        appartements = None
    elif service_type == 'apartment':
        appartements = Appartement.objects.all()
        vehicules = None
    else:
        vehicules = Vehicule.objects.all()[:3]  # Limite à 3 éléments pour l'affichage combiné
        appartements = Appartement.objects.all()[:3]
    
    context = {
        'service_type': service_type,
        'vehicules': vehicules,
        'appartements': appartements,
    }
    return render(request, 'core/services.html', context)
from .forms import ContactForm
from django.http import JsonResponse
def contact_api(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                send_mail(
                    subject=f"Contact: {form.cleaned_data['sujet']}",
                    message=f"Message de {form.cleaned_data['nom']}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['oumartom45@gmail.com'],
                )
                return JsonResponse({'status': 'success'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})
        return JsonResponse({'status': 'invalid', 'errors': form.errors})
    return JsonResponse({'status': 'invalid_method'}, status=405)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@require_POST
@csrf_exempt  # Temporaire pour le débogage
def contact_api(request):
    print("\n=== Nouvelle requête POST ===")
    print("Headers:", request.headers)
    print("META:", request.META)
    print("POST data:", request.POST)
    
    form = ContactForm(request.POST)
    
    if form.is_valid():
        try:
            print("Envoi d'email en cours...")
            send_mail(
                subject=f"Contact: {form.cleaned_data['sujet']}",
                message=f"De: {form.cleaned_data['nom']}\nEmail: {form.cleaned_data['email']}\n\nMessage:\n{form.cleaned_data['message']}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['oumartom45@gmail.com'],
                fail_silently=False,
            )
            print("Email envoyé avec succès!")
            return JsonResponse({'status': 'success'}, status=200)
        except Exception as e:
            print("Erreur d'envoi:", str(e))
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    print("Erreurs de formulaire:", form.errors)
    return JsonResponse({'status': 'invalid', 'errors': form.errors}, status=400)

def contact(request):
    print("Méthode de requête:", request.method)  # Debug
    
    if request.method == 'POST':
        print("Données POST reçues:", request.POST)  # Debug
        
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Formulaire valide. Envoi d'email...")  # Debug
            try:
                send_mail(
                    subject=f"Contact: {form.cleaned_data['sujet']}",
                    message=f"De: {form.cleaned_data['nom']} <{form.cleaned_data['email']}>\n\nMessage:\n{form.cleaned_data['message']}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['oumartom45@gmail.com'],
                    fail_silently=False,
                )
                print("success!")  # Debug
                messages.success(request, "success!")
                return redirect('core:contact')
            except Exception as e:
                print("Erreur d'envoi:", str(e))  # Debug
                messages.error(request, f"Erreur technique: {str(e)}")
        else:
            print("Erreurs de formulaire:", form.errors)  # Debug
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {'form': form})

def send_contact_email(message):
    # Email pour l'administrateur
    admin_subject = f"Nouveau message de contact: {message.sujet}"
    admin_message = f"""
    Nouveau message reçu depuis le formulaire de contact:
    
    Nom: {message.nom}
    Email: {message.email}
    Sujet: {message.sujet}
    
    Message:
    {message.message}
    
    ---
    Cet email a été envoyé automatiquement depuis le formulaire de contact.
    """
    
    send_mail(
        admin_subject,
        admin_message,
        settings.DEFAULT_FROM_EMAIL,
        ['oumartom45@gmail.com'],  # Email de destination
        fail_silently=False,
    )
    
    # Email de confirmation pour l'utilisateur
    user_subject = "Confirmation de réception de votre message"
    user_message = f"""
    Bonjour {message.nom},
    
    Nous avons bien reçu votre message concernant:
    "{message.sujet}"
    
    Nous vous contacterons dans les plus brefs délais.
    
    Cordialement,
    L'équipe ChadAuto&House Rental
    """
    
    send_mail(
        user_subject,
        user_message,
        settings.DEFAULT_FROM_EMAIL,
        [message.email],  # Email de l'expéditeur
        fail_silently=False,
    )
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['nom', 'email', 'sujet', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'placeholder': 'Votre nom complet'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Votre email'})
        self.fields['sujet'].widget.attrs.update({'placeholder': 'Sujet de votre message'})
        self.fields['message'].widget.attrs.update({'placeholder': 'Votre message ici...'})
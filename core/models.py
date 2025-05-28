from django.db import models

class ContactMessage(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    traite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sujet} - {self.nom}"

    class Meta:
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"
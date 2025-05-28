# from pyngrok import ngrok
# from django.conf import settings
# import os

# # Configurer Ngrok (remplacez par votre token)
# NGROK_AUTH_TOKEN = "2wsHvSETVgad4hnIaFsTB36JRlV_2vtfBYE93ncBKGEbqgvJx"  # À obtenir sur https://dashboard.ngrok.com/
# ngrok.set_auth_token(NGROK_AUTH_TOKEN)

# # Démarrer le tunnel
# public_url = ngrok.connect(8000, bind_tls=True).public_url
# print(f"\n=== Votre site est accessible via ===")
# print(f"URL Publique : {public_url}")
# print("=== Gardez ce terminal ouvert ===")
# print("Appuyez sur Ctrl+C pour arrêter\n")

# # Mettre à jour les paramètres Django automatiquement
# if hasattr(settings, 'ALLOWED_HOSTS'):
#     settings.ALLOWED_HOSTS.append(ngrok.get_tunnels()[0].public_url[8:])  # Retire 'https://'
#     settings.CSRF_TRUSTED_ORIGINS = [public_url]

from pyngrok import ngrok
import time
NGROK_AUTH_TOKEN = "2wsHvSETVgad4hnIaFsTB36JRlV_2vtfBYE93ncBKGEbqgvJx"  # À obtenir sur https://dashboard.ngrok.com/
ngrok.set_auth_token(NGROK_AUTH_TOKEN)
print("Configuration du tunnel Ngrok...")
tunnel = ngrok.connect(8000, bind_tls=True)
print(f"\n=== URL PUBLIQUE ===")
print(f"https://{tunnel.public_url[8:]}")  # Affiche sans 'https://'
print("\nInstructions:")
print("- Gardez ce terminal ouvert")
print("- Partagez le lien ci-dessus")
print("- Ctrl+C pour arrêter")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    ngrok.kill()
    print("\nTunnel fermé")
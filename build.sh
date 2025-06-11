
# 1. Installer les dépendances
pip install -r requirements.txt

# 2. Appliquer les migrations de base de données
python manage.py migrate

# 3. Collecter les fichiers statiques
python manage.py collectstatic --noinput

# 4. Autres commandes personnalisées si nécessaire
# python manage.py loaddata initial_data.json
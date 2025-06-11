pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py loaddata initial_data.json
python manage.py shell < create_superuser.py
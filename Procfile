web: gunicorn myproject.wsgi
release: python3 manage.py migrate
# Local environment
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

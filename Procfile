web: gunicorn application.wsgi
release: python3 manage.py migrate
# Local environment
release:python3 manage.py makemigrations
release:python3 manage.py runserver

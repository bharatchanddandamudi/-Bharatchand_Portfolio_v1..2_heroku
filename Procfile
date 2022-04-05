web: gunicorn myproject.wsgi
release: python manage.py migrate
# Local environment
git checkout -b add-migrations

python3 manage.py makemigrations
python3 manage.py migrate
git add -a
git commit -m "Database migrations"

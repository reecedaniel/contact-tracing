release: python manage.py migrate
web: gunicorn ContactTracing.wsgi --timeout 120 --log-file -

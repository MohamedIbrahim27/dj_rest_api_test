web: gunicorn dj_rest_api_test.wsgi
web: python manage.py migrate && gunicorn project.wsgi
web: python manage.py runserver 0.0.0.0:$PORT

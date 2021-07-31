
web: gunicorn DashboardBackend.wsgi --log-file -
celery: celery -A DashboardBackend worker --pool=solo -l info
celery beat: celery -A DashboardBackend beat --loglevel=info
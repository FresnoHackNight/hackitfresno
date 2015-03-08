web: python manage.py collectstatic --noinput && newrelic-admin run-program gunicorn hackitfresno.wsgi:application --bind=0.0.0.0:$PORT --workers=4 --log-level=info

release: sh -c 'python manage.py migrate && python manage.py loaddata track_data.json && python manage.py loaddata submission_data.json && python manage.py loaddata tracks.json && python manage.py loaddata speakers.json && python manage.py loaddata authors_data.json && python manage.py loaddata eventsgeneral.json && python manage.py loaddata eventsparallel.json'
web: gunicorn project_django.wsgi --log-file -
#web: bin/runsvdir-dyno
# release: cd bcm;python manage.py migrate --noinput
# web: cd bcm;gunicorn bcm.wsgi
#

web: cd bcm;npm install;python manage.py migrate --noinput;gunicorn bcm.wsgi


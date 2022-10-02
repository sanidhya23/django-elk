#!/bin/sh

# Check Database
# if [ "$DATABASE" = "postgres" ]
# then
#     echo "Waiting for postgres..."
#     while ! nc -z $SQL_HOST $SQL_PORT; do
#       sleep 0.1
#     done

#     echo "PostgreSQL started"
# fi

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --no-input --clear
# python manage.py createsuperuser --no-input
# python manage.py create_default_groups
# python manage.py create_default_users .prod.users.json
# python manage.py populate_models --top20
# python manage.py populate_models_people --top20
exec "$@"
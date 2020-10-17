#!/bin/bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for the DB..."

    # Using netcat to test DB connection
    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
        sleep 2
    done

    echo "PostgreSQL ready"
fi

# Run the Django migrations
python manage.py migrate
python manage.py loaddata bounce_data.json

exec "$@"

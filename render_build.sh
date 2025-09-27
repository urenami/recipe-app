#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput

# Force create admin superuser if not exists
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "adminpassword123")
EOF
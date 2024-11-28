import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
django.setup()

from django.contrib.auth.hashers import make_password
from recommender.models.user import User

def update_passwords():
    """Update all passwords in the database 
    to worik with the hashing algorithm"""
    users = User.objects.all()
    for user in users:
        user.password = make_password(user.password)
        user.save()

if __name__ == '__main__':
    update_passwords()
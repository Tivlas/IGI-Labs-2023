from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'email', 'date_of_birth', 'phone_number']
    USERNAME_FIELD = 'username'

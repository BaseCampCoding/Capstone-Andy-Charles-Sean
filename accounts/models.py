from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.apps import apps
# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES= [
    ('buyer', "Buyer"),
    ('seller', "Seller")
    ]

    roles = models.CharField(max_length=6, choices=ROLE_CHOICES, default="Buyer")
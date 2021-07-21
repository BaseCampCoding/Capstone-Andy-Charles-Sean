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

    def total_items(self):
        Posts = apps.get_model("post", "Post")
        all_posts_by_user = Posts.objects.filter(seller__id=self.id)
        total = 0
        for i in all_posts_by_user:
            total += i.total_item()
        return total
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.aggregates import Max
from django.urls import reverse
from django.conf import settings
from django_countries.fields import CountryField
# Create your models here.

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

class Post(models.Model):
    CATEGORIES= [
    ('tops', "Tops"),
    ('pants', "Pants"),
    ('shoes', "Shoes")
    ]
    
    image = models.ImageField(null=True, upload_to=None, height_field=None, width_field=None, max_length=100, )
    item  = models.CharField(max_length=64)
    categories = models.CharField(max_length=5, choices=CATEGORIES, default="Tops")
    seller = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    price = models.IntegerField()
  
    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])



class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)


    def __str__ (self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'
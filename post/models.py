from accounts.models import CustomUser
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

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
    favorite =  models.ManyToManyField(CustomUser, related_name='favorite', blank=True)
  
    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Post(models.Model):
    image = models.ImageField(null=True, upload_to=None, height_field=None, width_field=None, max_length=100, )
    item  = models.CharField(max_length=64)
    seller = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    price = models.IntegerField()

    def __str__(self):
        return self.item
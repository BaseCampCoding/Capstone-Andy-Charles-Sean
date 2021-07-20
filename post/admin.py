from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import Post

# Register your models here.

admin.site.register(Post)
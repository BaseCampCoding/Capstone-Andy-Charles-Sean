from django.contrib import admin
from .models import MorF, Post, Review

# Register your models here.




class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Review)
admin.site.register(MorF)

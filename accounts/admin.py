from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import CustomUser
# Register your models here.
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = [
        'username', 'first_name', 'last_name', 'email', 'roles', 'is_staff',
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('roles',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('roles',)}),
    )

admin.site.register(CustomUser, UserAdmin)
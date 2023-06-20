from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username','last_login','is_staff','is_active','is_superuser','phone']
    fieldsets = UserAdmin.fieldsets + (('Contact Info', {'fields':('phone',)}),)

admin.site.register(CustomUser, CustomUserAdmin)
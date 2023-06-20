from django.contrib import admin
from .models import recipe
# Register your models here.

class CustomrecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'cheff','ingredients','steps']
    
admin.site.register(recipe, CustomrecipeAdmin)
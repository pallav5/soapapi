from django.contrib import admin
from .models import Sector
# Register your models here.

class Sectoradmin(admin.ModelAdmin):
    list_display = ('user_name',)

admin.site.register(Sector, Sectoradmin)
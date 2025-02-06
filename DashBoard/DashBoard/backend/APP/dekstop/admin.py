from django.contrib import admin
from .models import Application, Desktop

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')

@admin.register(Desktop)
class DesktopAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
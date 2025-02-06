from rest_framework import serializers
from .models import Application, Desktop

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'name', 'icon', 'url']

class DesktopSerializer(serializers.ModelSerializer):
    applications = ApplicationSerializer(many=True, read_only=True)

    class Meta:
        model = Desktop
        fields = ['id', 'user', 'applications']
from django.db import models

class ToolBox(models.Model):
    name = models.CharField(max_length=100)
    icon_url = models.CharField(max_length=255)  # Stocke le lien vers l'icône
    color = models.CharField(max_length=20, default="#ffffff")  # Couleur de fond
    url = models.URLField(default="#") 
    height = models.IntegerField(default=100)
    width = models.IntegerField(default=150)
    x = models.IntegerField(default=500)
    y = models.IntegerField(default=500)

class Account(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    
    def __str__(self):
        return self.name

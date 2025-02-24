from django.db import models

class ToolBox(models.Model):
    name = models.CharField(max_length=100)
    icon_url = models.CharField(max_length=255)  # Stocke le lien vers l'icône
    color = models.CharField(max_length=20, default="#ffffff")  # Couleur de fond
    url = models.URLField(default="#") 
    height = models.IntegerField(default=100)
    width = models.IntegerField(default=150)

    def __str__(self):
        return self.name

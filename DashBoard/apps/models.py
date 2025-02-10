from django.db import models

class ToolBox(models.Model):
    name = models.CharField(max_length=100)
    icon_url = models.CharField(max_length=255)  # Stocke le lien vers l'icône
    color = models.CharField(max_length=20, default="#ffffff")  # Couleur de fond
    position_x = models.IntegerField(default=100)
    position_y = models.IntegerField(default=100)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Application(models.Model):
    """Représente une application sur le bureau."""
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Desktop(models.Model):
    """Représente le bureau d'un utilisateur avec ses applications."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    applications = models.ManyToManyField(Application, blank=True)

    def __str__(self):
        return f"Bureau de {self.user.username}"
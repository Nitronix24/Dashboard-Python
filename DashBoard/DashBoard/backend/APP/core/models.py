from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    """Modèle d'utilisateur personnalisé ajoutant un champ bio."""
    bio = models.TextField(blank=True, null=True)
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # nouveau related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set_permissions',  # nouveau related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    class Meta:
        app_label = "APP"

    def __str__(self):
        return self.username
    
class Icon(models.Model):
    icon_name = models.CharField(max_length=100)
    icon_image = models.ImageField(upload_to='frontend/Ressources/Icon/')

    class Meta:
        app_label = "APP"

    def __str__(self):
        return self.icon_name
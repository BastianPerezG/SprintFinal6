from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Permisos(models.Model):
    class Meta:
        permissions = (
            ('trabajador', 'Permisos exclusivo de los trabajadores'),
            ( 'cliente', 'Permisos exclusivo de los clientes')
        )

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images', default='default_image.png')

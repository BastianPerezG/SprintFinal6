from django.db import models

# Create your models here.

class Permisos(models.Model):
    class Meta:
        permissions = (
            ('trabajador', 'Permisos exclusivo de los trabajadores'),
            ( 'cliente', 'Permisos exclusivo de los clientes')
        )
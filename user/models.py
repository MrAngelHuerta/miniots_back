from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('administrador', 'Administrador'),
        ('usuario', 'Usuario'),
    )

    correo = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=20, choices=ROLES, default='usuario')

    telefono=models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.rol})"

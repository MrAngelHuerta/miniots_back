from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    correo = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

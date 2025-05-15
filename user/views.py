from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    Un ViewSet para ver y editar instancias de Usuario.
    """
    queryset = Usuario.objects.all()  # Los usuarios que queremos manejar (puedes filtrarlo si lo deseas)
    serializer_class = UsuarioSerializer  # Usamos el serializador para convertir el modelo en JSON


# Create your views here.

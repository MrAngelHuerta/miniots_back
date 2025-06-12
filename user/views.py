
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Usuario
from .serializers import UsuarioSerializer
from .permissions import IsAdmin, IsAdministrador

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [IsAdmin()]  # Solo los usuarios con rol 'admin' pueden listar usuarios
        elif self.action == 'retrieve':
            return [IsAdministrador()]  # Solo 'administrador' puede ver detalles individuales
        return [IsAuthenticated()]  # Otros métodos requieren autenticación normal

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    serializer = UsuarioSerializer(request.user)
    return Response(serializer.data)

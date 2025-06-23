from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import transaction
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny

from user.models import Usuario
from user.api.serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]
    
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                nombre = request.data["nombre"]
                username = request.data["username"]
                correo = request.data["correo"]
                password = request.data["password"]

                usuario = Usuario(
                    nombre=nombre,
                    username=username,
                    email=correo,
                    correo=correo,
                    rol="usuario",
                    password=make_password(password)
                )
                usuario.save()

            return Response(
                {
                    "estatus": "OK",
                    "respuesta": "Usuario Creado Exitosamente",
                    "usuario_id": usuario.id,
                },
                status=status.HTTP_200_OK,
            )
    
        except Exception as e:
            print("error", str(e))
            estatus = 98
            respuesta = "Error al crear al Usuario"
            return Response(
                {"estatus": estatus, "respuesta": respuesta + " " + str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    
    def list(selft, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_data = UsuarioSerializer(request.user).data

        filtered_data = {
            'id': user_data['id'],
            'nombre': user_data.get('nombre', ''),
            'correo': user_data.get('correo', ''),
            'rol': user_data.get('rol', ''),
        }
        return Response(filtered_data)

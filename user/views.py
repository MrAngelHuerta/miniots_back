from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import Usuario
from .serializers import UsuarioSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        correo = attrs.get("correo")
        password = attrs.get("password")

        print("🔍 Intentando autenticar con:", correo, password)

        try:
            user_obj = Usuario.objects.get(correo=correo)
            username = user_obj.username
            print("✅ Usuario encontrado:", username)
        except Usuario.DoesNotExist:
            print("❌ Usuario no encontrado con correo:", correo)
            raise serializers.ValidationError("Correo o contraseña incorrectos.")

        user = authenticate(username=username, password=password)

        if user is None:
            print("❌ Falló la autenticación con:", username)
            raise serializers.ValidationError("Correo o contraseña incorrectos.")

        print("✅ Autenticación exitosa para:", username)

        data = super().validate({
            "username": username,
            "password": password
        })

        data.update({
            "correo": user.correo,
            "nombre": user.nombre,
        })

        print("📦 Datos del token generados:", data)

        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]


@api_view(['GET'])
@permission_classes([AllowAny])
def current_user(request):
    serializer = UsuarioSerializer(request.user)
    return Response(serializer.data)

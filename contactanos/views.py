from rest_framework import viewsets
from .models import MensajeContacto
from .serializers import MensajeContactoSerializer
from rest_framework.permissions import AllowAny

class ContactoViewSet(viewsets.ModelViewSet):
    queryset = MensajeContacto.objects.all().order_by('-fecha')
    serializer_class = MensajeContactoSerializer
    permission_classes = [AllowAny]  # Puedes cambiar a IsAuthenticated si quieres protegerlo

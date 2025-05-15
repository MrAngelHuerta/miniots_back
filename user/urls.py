from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet

# Configuración del router de DRF
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Incluye todas las rutas del ViewSet
]

from rest_framework.routers import SimpleRouter
from user.api.views import (UsuarioViewSet)

router_user = SimpleRouter()

router_user.register(prefix="usuarios", basename="usuario", viewset=UsuarioViewSet)
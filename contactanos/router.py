from rest_framework.routers import SimpleRouter
from contactanos.views import (ContactoViewSet)

router_contacto = SimpleRouter()

router_contacto.register(prefix="contacto", basename="mensajes", viewset=ContactoViewSet)
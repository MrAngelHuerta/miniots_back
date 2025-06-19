from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        #Diferenciacion de logueo entre email y username
        user = None
        if '@' in username:
            try:
                user = Usuario.objects.get(correo=username)
            except Usuario.DoesNotExist:
                return None
        else:
            try:
                user = Usuario.objects.get(username=username)
            except Usuario.DoesNotExist:
                return None

        # Validar contraseña
        if user and user.check_password(password):
            return user
        return None
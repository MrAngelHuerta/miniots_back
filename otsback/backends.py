from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = None
        if username is None or password is None:
            return None
        
        # Diferenciar login por email o username
        if '@' in username:
            try:
                # Cambia 'correo' por 'email' si es ese el campo correcto
                user = Usuario.objects.get(email=username)
            except Usuario.DoesNotExist:
                return None
        else:
            try:
                user = Usuario.objects.get(username=username)
            except Usuario.DoesNotExist:
                return None

        # Validar contraseña y si el usuario puede autenticarse (activo)
        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user

        return None

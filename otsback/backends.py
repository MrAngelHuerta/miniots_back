from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = None
        if username is None or password is None:
            return None
        
        if '@' in username:
            try:
                user = Usuario.objects.get(email=username)
            except Usuario.DoesNotExist:
                return None
        else:
            try:
                user = Usuario.objects.get(username=username)
            except Usuario.DoesNotExist:
                return None

        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user

        return None

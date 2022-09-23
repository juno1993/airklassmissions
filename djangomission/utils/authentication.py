from rest_framework.authentication import TokenAuthentication

from accounts.models import CustomUserToken


class MasterAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        model = CustomUserToken
        try:
            token = model.objects.get(key=key)
        except model.DoesNotExist:
            return None
        """
        유저가 마스터인지 확인
        """
        if not hasattr(token.user, 'contentshub_master'):
            return None
        return token.user, token


class UserAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        model = CustomUserToken
        try:
            token = model.objects.get(key=key)
        except model.DoesNotExist:
            return None
        return token.user, token

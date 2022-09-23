from rest_framework import exceptions

from accounts.models import CustomUserToken, User
from accounts.ser import UserSerializer


def user_login(request, **kwargs):
    data = request.data
    user = User.objects.filter(username=data.get('username'))
    if not user.exists():
        raise exceptions.AuthenticationFailed('아이디에 해당하는 유저가 없습니다.')

    user = user.first()

    if not user.check_password(data.get('password')):
        raise exceptions.AuthenticationFailed('비밀번호가 일치하지 않습니다.')
    CustomUserToken.objects.get_or_create(user=user)
    return UserSerializer(user).data

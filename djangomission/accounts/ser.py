

from rest_framework import serializers

from accounts.models import User
from contentshub.models import Master


class UserMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(source='token.key')
    master = UserMasterSerializer(source='contentshub_master')

    class Meta:
        model = User
        exclude = (
            'password',
        )

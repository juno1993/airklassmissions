



from rest_framework import serializers

from contentshub.models import Klass


class KlassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klass
        fields = '__all__'





from rest_framework import serializers

from community.ser import QuestionSerializer
from contentshub.models import Klass


class KlassSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(source='community_question', many=True)

    class Meta:
        model = Klass
        fields = '__all__'

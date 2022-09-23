

from rest_framework import serializers

from community.models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(source='community_answer.first')

    class Meta:
        model = Question
        fields = '__all__'

from models import Question
from models import AnswerHistory
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class QuestionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Question
        fields = ('id', 'user', 'question', 'left', 'right', 'left_count', 'right_count', 'create_time', 'url')

class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('user', 'question', 'left', 'right', 'url')

class AnswerHistorySerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = AnswerHistory
        fields = ('user', 'question', 'answer')


class AnswerHistoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerHistory
        fields = ('user', 'question', 'answer')

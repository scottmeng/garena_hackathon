from models import Question
from models import AnswerHistory
from django.contrib.auth.models import User
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question', 'left', 'right', 'left_count', 'right_count', 'create_time')

class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('user', 'question', 'left', 'right')

class AnswerHistorySerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = AnswerHistory
        fields = ('user', 'question', 'answer')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class AnswerHistoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerHistory
        fields = ('user', 'question', 'answer')

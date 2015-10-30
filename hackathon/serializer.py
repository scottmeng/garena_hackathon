__author__ = 'Moonlight'

from models import Question
from models import AnswerHistory

from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_id', 'left', 'right' ,'create_time')

class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_id', 'left', 'right')

class AnswerHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerHistory
        fields = ('user', 'question', 'answer')

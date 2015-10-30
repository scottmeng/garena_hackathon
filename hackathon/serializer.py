__author__ = 'Moonlight'


from models import Answer
from models import Question
from models import AnswerHistory

from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question', 'left', 'right', 'view_count','answer_count',
                  'ignore_count','discard_count','create_time','enable')

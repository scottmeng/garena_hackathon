from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Answer(models.Model):
    answer = models.CharField(max_length=128)
    class Meta:
        db_table = 'answer_tab'

class Question(models.Model):
    question = models.CharField()
    answer_left = models.ForeignKey(Answer, on_delete=models.PROTECT)
    answer_right = models.ForeignKey(Answer, on_delete=models.PROTECT)
    create_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'question_tab'

class AnswerHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    class Meta:
        db_table = 'answer_history_tab'
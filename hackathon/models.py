from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Answer(models.Model):
    answer = models.CharField(max_length=128)
    enable = models.BooleanField(default=True)
    class Meta:
        db_table = 'answer_tab'

class Question(models.Model):
    question = models.CharField(max_length=2555)
    left = models.ForeignKey(Answer, on_delete=models.PROTECT, related_name='left')
    right = models.ForeignKey(Answer, on_delete=models.PROTECT, related_name='right')
    view_count = models.PositiveIntegerField(default=0)
    answer_count = models.PositiveIntegerField(default=0)
    ignore_count = models.PositiveIntegerField(default=0)
    discard_count = models.PositiveIntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    enable = models.BooleanField(default=True)
    class Meta:
        db_table = 'question_tab'

class AnswerHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    answer = models.ForeignKey(Answer, on_delete=models.PROTECT)
    enable = models.BooleanField(default=True)
    class Meta:
        db_table = 'answer_history_tab'
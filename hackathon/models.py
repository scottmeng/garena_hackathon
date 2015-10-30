# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class User_Profile(models.Model):
    GENDERS = (('male', 'Male'),('female','Female'))
    user = models.OneToOneField(User,primary_key=True)
    avatar = models.CharField(max_length=1024)
    gender = models.CharField(max_length=20, null=True, blank=True, choices=GENDERS)
    class Meta:
        db_table = 'user_profile'


class Question(models.Model):
    question = models.CharField(max_length=2555)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    left = models.CharField(max_length=128)
    right = models.CharField(max_length=128)
    view_count = models.PositiveIntegerField(default=0)
    left_count = models.PositiveIntegerField(default=0)
    right_count = models.PositiveIntegerField(default=0)
    report_count = models.PositiveIntegerField(default=0)
    skip_count = models.PositiveIntegerField(default=0)
    url =  models.URLField(max_length=512, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    enable = models.BooleanField(default=True)
    class Meta:
        db_table = 'question_tab'

class AnswerHistory(models.Model):
    NO_ANSWER = 0
    LEFT = 1
    RIGHT = 2
    SKIP = 3
    REPORT = 4
    ANSWER_CHOICES = ((NO_ANSWER, 'No_Answer'),
                    (LEFT, 'Left'),
                    (RIGHT, 'Right'),
                    (SKIP, 'Skip'),
                    (REPORT, 'Report')
                    )
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    answer = models.PositiveIntegerField(choices=ANSWER_CHOICES,default=NO_ANSWER)
    enable = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'answer_history_tab'

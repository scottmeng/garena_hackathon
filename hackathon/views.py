from django.shortcuts import render, redirect
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from hackathon import models
from hackathon.serializer import *
from rest_framework.decorators import api_view
from django.db.models import F
from hackathon.models import AnswerHistory
from hackathon.serializer import QuestionSerializer
from django.contrib.auth.models import User

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@login_required(login_url='/login/')
def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def login(request):
    return render(request, 'login.html')

def login_failed(request):
    return render_to_response('login_failed.html', context_instance=RequestContext(request))

def logout(request):
    auth_logout(request)
    return redirect('/login/')

@login_required()
@csrf_exempt
def questions_list(request):
    if request.method == 'GET':
        my_answers = models.AnswerHistory.objects.filter(user_id=request.user.id)
        my_answers_id = list(x.question_id for x in my_answers)
        questions = models.Question.objects.exclude(id__in=my_answers_id
                                                    ).order_by('-create_time')[:10]
        serializer = QuestionSerializer(questions, many=True)
        return JSONResponse(serializer.data)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['user'] = request.user.id
        serializer = QuestionCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@login_required()
@csrf_exempt
def questions_edit(request,pk):
    try:
        question = models.Question.objects.get(pk=pk)
    except models.Question.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['user_id'] = request.user.id
        serializer = QuestionCreateSerializer(question, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        question.delete()
        return HttpResponse(status=204)

@login_required()
@csrf_exempt
def my_questions(request):
    if request.method == 'GET':
        questions = models.Question.objects.filter(user_id=request.use.id
                                                   ).order_by('-create_time')[:10]
        serializer = QuestionSerializer(questions, many=True)
        return JSONResponse(serializer.data)

@login_required()
@csrf_exempt
def user(request):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=request.user.id)
            serializer = UserSerializer(user)
            return JSONResponse(serializer.data)
        except models.User.DoesNotExist:
            return HttpResponse(status=404)


@csrf_exempt
@login_required(login_url='/login/')
def answers_list(request):
    if request.method == 'GET':
        answers = AnswerHistory.objects.filter(user=request.user)
        serializer = AnswerHistorySerializer(answers, many=True)
        return JSONResponse(serializer.data)

@login_required(login_url='/login/')
@csrf_exempt
def answers(request, question_id):
    try:
        question = models.Question.objects.get(pk=question_id)
    except models.Question.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['user'] = request.user.pk
        data['question'] = question.pk
        serializer = AnswerHistoryCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

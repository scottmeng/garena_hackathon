from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

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
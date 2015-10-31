from django.core.management.base import BaseCommand
from urllib import FancyURLopener
import urllib2
import json
from hackathon import models
from django.contrib.auth.models import User
import operator
from django.db import transaction
from urllib import FancyURLopener
import json
import re
from urllib import urlencode
import urllib2

question_list = [
    ['Is PHP the best programming language?','Yes','No'],
    ['Garena is the best company in the World.','Yes','Yes'],
    ['Kissed any one of your Facebook friends?','Yes','No'],
    ['Kissed someone you didnt like?','Yes','No'],
    ['Been fired from a job?','Yes','No'],
    ['Kissed in the rain?','Yes','No'],
    ['Broken a bone?','Yes','No'],
    ['Donated Blood?','Yes','No'],
    ['Believe in Love?','Yes','No'],
    ['Forgotten your own birthday?','Yes','No'],
    ['Been healthy and slept more than 12 hrs?','Yes','No'],
    ['Been in the presence of a human birth?','Yes','No'],
    ['Been in a race of 5K or more?','Yes','No'],
    ['Been on TV?','Yes','No'],
    ['Smoked a cigar?','Yes','No'],
    ['Sat on a rooftop?','Yes','No'],
    ['Shot a gun?','Yes','No'],
    ['Still love someone you shouldnt?','Yes','No'],
    ['Been arrested or taken to jail?','Yes','No'],
    ['Have you ever failed a quiz','Yes','No'],
    ['Ever cheated on someone?','Yes','No'],
    ['Are you a procrastinator?','Yes','No'],
    ['Do you believe in Karma and Destiny?','Yes','No'],
    ['If abandoned alone in the wilderness would you survive?','Yes','No'],
    ['Ever had a crush on a guy?','Yes','No'],
    ['Peed your pants in public?','Yes','No'],
]

class Command(BaseCommand):
    def handle(self, *args, **options):
        users = models.User.objects.all().order_by('id')
        count = 0
        if users:
            user = users[0]
            for question in question_list:
                count=count+1
                print(count)
                url = fetch_related_image(question[0]) or ''
                models.Question.objects.create(question=question[0],
                                               left=question[1],
                                               right=question[2],
                                               user=user,
                                               url=url,)

class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

def fetch_related_image(question):
    searchTerm = question
    params = {'v': '1.0', 'q': searchTerm.encode('utf8'), 'start': 0, 'userip': '111.223.103.130'}
    params = urlencode(params)
    params = params.replace(' ','%20')
    url = ('https://ajax.googleapis.com/ajax/services/search/images?' + params)
    print(url)
    request = urllib2.Request(url, None)
    response = urllib2.urlopen(request)
    results = json.load(response)
    data = results['responseData']
    dataInfo = data['results']

    for myUrl in dataInfo:
        print(myUrl['unescapedUrl'])
        return myUrl['unescapedUrl']
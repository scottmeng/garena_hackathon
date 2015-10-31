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
    ['garena is the best it company in singapore','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['garena is the best it company in singapore','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Is PHP the best programming language?','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['Garena is the best IT company in Singapore','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
    ['zheng naijia','Yes','No'],
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
import json
import os
import decimal
from decimal import Decimal
import logging
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.core.mail import EmailMessage
from django.db.models import Sum
from django.utils.timezone import now, localtime
from django.forms import fields
from django.db.models import Q
from django.db.models import F
from django.db import transaction
import os
import sys
import time
from urllib import FancyURLopener
import urllib2
import json

class Command(BaseCommand):
    def handle(self, *args, **options):

        # Define search term
        searchTerm = "hello world"

        # Replace spaces ' ' in search term for '%20' in order to comply with request
        searchTerm = searchTerm.replace(' ','%20')


        # Start FancyURLopener with defined version
        class MyOpener(FancyURLopener):
            version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
        myopener = MyOpener()

        # Set count to 0
        count= 0

        for i in range(0,10):
            # Notice that the start changes for each iteration in order to request a new set of images for each loop
            url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q='+searchTerm+'&start='+str(i*4)+'&userip=MyIP')
            print url
            request = urllib2.Request(url, None, {'Referer': 'testing'})
            response = urllib2.urlopen(request)

            # Get results using JSON
            results = json.load(response)
            data = results['responseData']
            dataInfo = data['results']

            # Iterate for each result and get unescaped url
            for myUrl in dataInfo:
                count = count + 1
                print myUrl['unescapedUrl']

                myopener.retrieve(myUrl['unescapedUrl'],str(count)+'.jpg')

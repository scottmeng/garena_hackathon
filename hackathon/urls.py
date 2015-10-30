from django.conf.urls import include, url
from hackathon import views

urlpatterns = [
    url(r'^$', 'hackathon.views.index'),
]
from django.conf.urls import include, url
from hackathon import views

urlpatterns = [
    url(r'^$', 'hackathon.views.index'),
    url(r'^login/$', 'hackathon.views.login'),
    url(r'^logout/$', 'hackathon.views.logout'),

    url(r'^answers/$', 'hackathon.views.answers_list'),
    url(r'^answers/(?P<question_id>\d+)/$', 'hackathon.views.answers')
]
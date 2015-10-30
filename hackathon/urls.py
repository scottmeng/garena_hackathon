from django.conf.urls import include, url
from hackathon import views

urlpatterns = [
    url(r'^$', 'hackathon.views.index'),
    url(r'^login/$', 'hackathon.views.login'),
    url(r'^logout/$', 'hackathon.views.logout'),
    url(r'^questions/$', 'hackathon.views.questions_list'),
    url(r'^questions/(?P<pk>\d+)/$','hackathon.views.questions_edit'),
    url(r'^questions/me/$','hackathon.views.my_questions'),
    url(r'^questions/search/$', 'hackathon.views.questions_search'),
    url(r'^me/$','hackathon.views.user'),
    url(r'^answers/$', 'hackathon.views.answers_list'),
    url(r'^answers/(?P<question_id>\d+)/$', 'hackathon.views.answers'),
]

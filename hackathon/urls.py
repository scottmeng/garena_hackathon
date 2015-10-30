from django.conf.urls import include, url
from hackathon import views

urlpatterns = [
    url(r'^$', 'hackathon.views.index'),
    url(r'^login/$', 'hackathon.views.login'),
    url(r'^logout/', 'hackathon.views.logout'),
    url(r'^questions/$', 'hackathon.views.questions_list'),
    url(r'^questions/(?P<pk>\d+)/$','hackathon.views.questions_edit'),
    url(r'^questions/me/$','hackathon.views.my_questions'),
]
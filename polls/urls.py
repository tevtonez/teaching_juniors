from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.PollsIndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.QuestionDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.QuestionResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]

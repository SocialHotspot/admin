from django.conf.urls import patterns, include, url
from statistics.views import facebook

urlpatterns = patterns('',
    url(r'^facebook/$', facebook, name='facebook'),
)
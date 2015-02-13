from django.conf.urls import patterns, include, url

from api.views import hotspot

urlpatterns = patterns('',
    url(r'^hotspots/(?P<pk>\d+)/$', hotspot, name='detail'),
)
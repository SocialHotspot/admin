from django.conf.urls import patterns, include, url

from api.views import hotspot

urlpatterns = patterns('',
    url(r'^hotspots/(?P<id>\d+)/?$', hotspot, name='detail'),
)
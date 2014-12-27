from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^clients/', include('clients.urls', namespace='clients')),
)
from django.conf.urls import patterns, include, url

from clients.views import ClientList, add

urlpatterns = patterns('',
    url(r'^$', ClientList.as_view(), name='overview'),
    url(r'^add/$', add, name='add'),
)
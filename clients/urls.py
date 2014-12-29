from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from clients.views import ClientList, ClientDetail, add

urlpatterns = patterns('',
    url(r'^$', login_required(ClientList.as_view()), name='overview'),
    url(r'^detail/(?P<slug>[\w-]+)/$', login_required(ClientDetail.as_view()), name='detail'),
    url(r'^add/$', add, name='add'),
)
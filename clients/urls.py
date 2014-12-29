from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from clients.views import ClientList, ClientDetail, add, portal_preview

urlpatterns = patterns('',
    url(r'^$', login_required(ClientList.as_view()), name='overview'),
    
    url(r'^detail/(?P<slug>[\w-]+)/$', login_required(ClientDetail.as_view()), name='detail'),
    url(r'^add/$', add, name='add'),
    
    url(r'^portal/(?P<client_id>\d+)/$', portal_preview, name='portal_preview'),
)
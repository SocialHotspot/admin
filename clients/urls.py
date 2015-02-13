from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from clients.views import ClientList
from clients.views import ClientDetail
from clients.views import hotspots
from clients.views import add_hotspot
from clients.views import portal
from clients.views import add
from clients.views import portal_preview
from clients.views import set_portal_settings

urlpatterns = patterns('',
    url(r'^$', login_required(ClientList.as_view()), name='overview'),
    
    url(r'^add/$', add, name='add'),
    
    url(r'^detail/(?P<slug>[\w-]+)/$', login_required(ClientDetail.as_view()), name='detail'),
    
    url(r'^detail/(?P<slug>[\w-]+)/hotspots$', hotspots, name='hotspots'),
    url(r'^detail/(?P<slug>[\w-]+)/add_hotspot$', add_hotspot, name='add_hotspot'),
    
    url(r'^detail/(?P<slug>[\w-]+)/portal$', portal, name='portal'),
    url(r'^detail/(?P<slug>[\w-]+)/portal_settings$', set_portal_settings, name='set_portal_settings'),
    
    url(r'^portal/(?P<slug>[\w-]+)/$', portal_preview, name='portal_preview')
)
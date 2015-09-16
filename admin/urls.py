from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

urlpatterns = patterns('',
	url(r'^$', RedirectView.as_view(url='/clients/')),

	url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^clients/', include('clients.urls', namespace='clients')),
    url(r'^stock/', include('stock.urls', namespace='stock')),
    
    url(r'^unifi/', include('unifi_control.urls', namespace='unifi')),
    
    url(r'^statistics/', include('statistics.urls', namespace='statistics')),
)
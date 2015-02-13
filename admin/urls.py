from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

urlpatterns = patterns('',
	url(r'^$', RedirectView.as_view(url='/clients/')),

	url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^clients/', include('clients.urls', namespace='clients')),
    
    url(r'^api/', include('api.urls', namespace='api')),
)
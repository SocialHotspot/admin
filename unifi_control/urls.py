from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from unifi_control.views import create_site, set_general_settings, set_guest_portal, add_wlans

urlpatterns = patterns('',
    url(r'^create-site/$', create_site, name='create-site'),
    url(r'^set-general-settings/$', set_general_settings, name='set-general-settings'),
    url(r'^set-guest-portal/$', set_guest_portal, name='set-guest-portal'),
    url(r'^add-wlans/$', add_wlans, name='add-wlans'),
    
)
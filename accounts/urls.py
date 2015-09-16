from django.conf.urls import patterns, url

from accounts.views import settings, add_device

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', { 'template_name': 'accounts/login.html' }, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', { 'next_page': '/accounts/login' }, name='logout'),
    
    url(r'^$', settings, name='settings'),
    url(r'^add_device/$', add_device, name='add_device'),
)
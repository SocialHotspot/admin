from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from stock.views import overview, add

urlpatterns = patterns('',
    url(r'^$', overview, name='overview'),
    
    url(r'^add/$', add, name='add')
)
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from stock.views import StockList, add

urlpatterns = patterns('',
    url(r'^$', login_required(StockList.as_view()), name='overview'),
    
    url(r'^add/$', add, name='add')
)
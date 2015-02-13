from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from clients.models import Hotspot
	
class StockList(ListView):
    model = Hotspot
    context_object_name = 'hotspots'
    
    template_name = 'stock/overview.html'
    
    def get_queryset(self):
        return Hotspot.objects.filter(client_id = None)
    
@login_required   
def add(request):
	data = { key: request.POST[key] for key in request.POST if key != 'csrfmiddlewaretoken' }
	
	hotspot = Hotspot(**data)
	hotspot.save()
	
	return HttpResponseRedirect(reverse('stock:overview'))
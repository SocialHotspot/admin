from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required

from clients.models import Hotspot
from unifi_control.models import UnifiController

from urllib2 import HTTPError
from django.contrib import messages
        
@login_required
def overview(request):
	
	controllers = UnifiController.get_with_stock()
	
	aps = []
	
	for c in controllers:
		try:
			c = c.controller()
			aps += c.get_aps()
			
		except HTTPError:
			messages.error(request, "The login credentials for controller '"+ c.name +"' are incorrect.")
	
	return render(request, 'stock/overview.html', {
	    'aps': aps
	})
    
@login_required   
def add(request):
	data = { key: request.POST[key] for key in request.POST if key != 'csrfmiddlewaretoken' }
	
	hotspot = Hotspot(**data)
	hotspot.save()
	
	return HttpResponseRedirect(reverse('stock:overview'))
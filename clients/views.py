from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.views.generic import ListView, DetailView

from clients.models import Client, Hotspot
from unifi_control.models import UnifiController

from django.contrib.auth.decorators import login_required
from django.contrib import messages

class ClientList(ListView):
    model = Client
    context_object_name = 'clients'
    
    template_name = 'clients/overview.html'
 
class ClientDetail(DetailView):
    model = Client
    context_object_name = 'client'
    
    template_name = 'clients/detail.html'

@login_required
def hotspots(request, slug):
	client = Client.objects.get(slug = slug)
	hotspots = client.hotspots.all()
	
	return render(request, 'clients/hotspots.html', {
	    'client': client,
	    'hotspots': hotspots
	})
	
@login_required
def portal(request, slug):
	client = Client.objects.get(slug = slug)
	
	return render(request, 'clients/portal.html', {
	    'client': client,
	    'portal': client.portal
	})
	
@login_required
def set_portal_settings(request, slug):
	client = Client.objects.get(slug = slug)
	portal = client.portal
	
	setting = request.POST['setting']
	value = request.POST['value']
	
	booleanFields = ['facebook_enabled', 'password_enabled']
	valueFields = ['facebook_page_id', 'guest_password']
	
	if not (setting in booleanFields):
		
		if setting in valueFields:
			setattr(portal, setting, value)
		else:
			setattr(portal, setting, (value == 'true'))
			
	else:
		if setting == 'facebook_enabled' and value == 'false':
			portal.facebook_page_id = None
				
		elif setting == 'password_enabled' and value == 'false':
			portal.guest_password = None
	
	portal.save()
	
	return HttpResponse()
	
@login_required   
def add_hotspot(request, slug):
	client = Client.objects.get(slug = slug)
	
	controllers = UnifiController.get_with_stock()
	aps = []
	
	existing_macs = [ hotspot.mac_address for hotspot in Hotspot.objects.all() ]
	
	for c in controllers:
		c = c.controller()
		aps += c.get_aps()
	
	available = [ ap for ap in aps if ap['mac'] not in existing_macs ]
	
	if len(available):
		ap = available[0]
		
		hotspot = Hotspot(mac_address = ap['mac'], client_id = client.id, external_id = (Hotspot.latest_id() + 1))
		hotspot.save()
	else:
		messages.error(request, 'There are no hotspots left in stock.')
	
	return HttpResponseRedirect(reverse('clients:hotspots', kwargs={ 'slug': client.slug }))

@login_required   
def add(request):
	data = { key: request.POST[key] for key in request.POST if key != 'csrfmiddlewaretoken' }
	
	client = Client(**data)
	client.save()
	
	return HttpResponseRedirect(reverse('clients:overview'))
	
@login_required
def portal_preview(request, slug):
	client = Client.objects.get(slug = slug)
	
	return render(request, 'clients/portal/cilis/start.html', {
	    'client': client
	})
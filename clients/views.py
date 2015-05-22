from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.views.generic import ListView, DetailView

from clients.models import Client, Hotspot
from unifi_control.models import UnifiController

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages
from django.core import serializers

import re, json

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
	
	if client.unifi_site:	
		hotspots = client.hotspots.all()
		
		return render(request, 'clients/hotspots.html', {
		    'client': client,
		    'hotspots': hotspots
		})
		
	else:
		# Setup is required
		if client.city:
			unifi_site_id = client.company_name +' '+ client.city
		else:
			unifi_site_id = client.company_name
		
		unifi_site_id = re.sub(r'[^A-Za-z0-9\-]', '', unifi_site_id.lower().replace(' ', ''))[:24]
		
		return render(request, 'clients/setup.html', {
		    'client': client,
		    'unifi_site_id': unifi_site_id
		})
	
@login_required
def portal(request, slug):
	client = Client.objects.get(slug = slug)
	
	if request.method == 'POST' and 'logo' in request.FILES:
		client.portal.logo = request.FILES['logo']
		client.portal.save()
	
	return render(request, 'clients/portal.html', {
	    'client': client,
	    'portal': client.portal,
	    
	    'preview_hotspot': client.hotspots.first()
	})
	
@login_required
def set_portal_settings(request, slug):
	client = Client.objects.get(slug = slug)
	portal = client.portal
	
	setting = request.POST['setting']
	value = request.POST['value']
	
	booleanFields = ['facebook_enabled', 'password_enabled', 'network_password_enabled']
	valueFields = ['facebook_page_id', 'guest_password', 'wpa_password', 'background_color', 'logo_margin']
	
	if not (setting in booleanFields):
		
		if setting in valueFields:
			if setting == 'wpa_password' and len(value) < 8:
				value = None
			elif setting == 'wpa_password' and len(value) >= 8:
				controller = client.unifi_controller.controller(client.unifi_site)
			
				controller.set_wpa_password(value)
					
			setattr(portal, setting, value)
		else:
			setattr(portal, setting, (value == 'true'))
			
	else:
		if setting == 'facebook_enabled' and value == 'false':
			portal.facebook_page_id = None
				
		elif setting == 'password_enabled' and value == 'false':
			portal.guest_password = None
			
		elif setting == 'network_password_enabled' and value == 'false':
			portal.wpa_password = None
			
			controller = client.unifi_controller.controller(client.unifi_site)
			controller.set_wpa_password(False)
	
	portal.save()
	
	return HttpResponse()
	
@login_required   
def add_hotspot(request, slug):
	client = Client.objects.get(slug = slug)
	
	hotspots = add_hotspots_from_stock(client, 1)
	
	if not hotspots:
		messages.error(request, 'There are no hotspots left in stock.')
	
	return HttpResponseRedirect(reverse('clients:hotspots', kwargs={ 'slug': client.slug }))

@csrf_exempt
def add_hotspots_ajax(request, slug):
	client = Client.objects.get(slug = slug)
	number_of_aps = int(request.POST.get('number_of_aps', 1))
	
	hotspots = add_hotspots_from_stock(client, number_of_aps)
	
	if hotspots:
		return HttpResponse(json.dumps({ 'hotspots': hotspots }), content_type='application/json')
	else:
		return HttpResponse(json.dumps({ 'error': "Not enough hotspots in stock" }), content_type='application/json')
	
def add_hotspots_from_stock(client, number_of_aps):
	controllers = UnifiController.get_with_stock()
	aps = []
	
	existing_macs = [ hotspot.mac_address for hotspot in Hotspot.objects.all() ]
	
	for c in controllers:
		c = c.controller()
		aps += c.get_aps()
	
	available = [ ap for ap in aps if ap['mac'] not in existing_macs ]

	if len(available) >= number_of_aps:
		hotspots = []
	
		for ap in range(0, number_of_aps):
			ap = available[ap]
		
			hotspot = Hotspot(mac_address = ap['mac'], client_id = client.id, external_id = (Hotspot.latest_id() + 1))
			hotspot.save()
			
			hotspots.append(hotspot)
			
		hotspots = [ { 'external_id': hotspot.external_id, 'mac_address': hotspot.mac_address } for hotspot in hotspots ]
			
		return hotspots
	else:
		return False
		
@csrf_exempt
def set_unifi_site(request, slug):
	client = Client.objects.get(slug = slug)
	
	site_id = request.POST['unifi_site_id']
	controller_id = request.POST['unifi_controller']

	client.unifi_site = site_id
	client.unifi_controller_id = controller_id
	
	client.save()
	
	return HttpResponse(True)

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
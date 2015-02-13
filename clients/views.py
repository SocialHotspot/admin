from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.views.generic import ListView, DetailView
from clients.models import Client, Hotspot

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
def add_hotspot(request, slug):
	client = Client.objects.get(slug = slug)
	
	hotspot = Hotspot.objects.filter(client_id = None).first()
	
	if hotspot:
		client.hotspots.add(hotspot)
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
	
	return render(request, 'clients/portal/index.html', {
	    'client': client
	})
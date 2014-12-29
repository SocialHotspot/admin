from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views.generic import ListView, DetailView
from clients.models import Client

from django.contrib.auth.decorators import login_required

class ClientList(ListView):
    model = Client
    context_object_name = 'clients'
    
    template_name = 'clients/overview.html'
 
class ClientDetail(DetailView):
    model = Client
    context_object_name = 'client'
    
    template_name = 'clients/detail.html'

@login_required   
def add(request):
	data = { key: request.POST[key] for key in request.POST if key != 'csrfmiddlewaretoken' }
	
	client = Client(**data)
	client.save()
	
	return HttpResponseRedirect(reverse('clients:overview'))
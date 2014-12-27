from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views.generic import ListView
from clients.models import Client

class ClientList(ListView):
    model = Client
    context_object_name = 'clients'
    
    template_name = 'clients/overview.html'
    
def add(request):
	data = { key: request.POST[key] for key in request.POST if key != 'csrfmiddlewaretoken' }
	
	client = Client(**data)
	client.save()
	
	return HttpResponseRedirect(reverse('clients:overview'))
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

import json
from django.forms.models import model_to_dict

from django.core.exceptions import ObjectDoesNotExist

from clients.models import Hotspot

@login_required
def hotspot(request, id):
	try:
		hotspot = Hotspot.objects.get(external_id = id)
		data = model_to_dict(hotspot)
		
		data.pop('id', None)
		
		client = model_to_dict(hotspot.client)
		fields = ['company_name', 'contact_name', 'email', 'street', 'number', 'postal', 'city', 'country']
		
		data['client'] = { key: client[key] for key in fields }
		
	except ObjectDoesNotExist:
		data = { 'error': 'No hotspot found' }
	
	return HttpResponse(json.dumps(data), content_type='application/json')
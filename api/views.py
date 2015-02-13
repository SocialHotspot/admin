from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

from clients.models import Hotspot

@login_required
def hotspot(request, pk):
	hotspot = Hotspot.objects.get(pk = pk)
	
	return HttpResponse(serializers.serialize('json', [hotspot]), content_type='application/json')
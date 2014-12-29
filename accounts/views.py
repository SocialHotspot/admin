from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from accounts.models import AdminDevice

@login_required
def settings(request):
	return render(request, 'accounts/settings.html', {
        'devices': request.user.devices
    })
    
@login_required
def add_device(request):
	data = { key: request.POST[key] for key in request.POST if key != 'csrfmiddlewaretoken' }
	
	device = AdminDevice(user=request.user, **data)
	device.mac_address = device.mac_address.upper()
	
	device.save()
	
	return HttpResponseRedirect(reverse('accounts:settings'))
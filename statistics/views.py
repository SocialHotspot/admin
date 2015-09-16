from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def facebook(request):		
	return render(request, 'statistics/facebook.html')
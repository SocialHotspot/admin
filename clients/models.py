from django.db import models
from django.db.models.signals import post_save

# Clients		
class Client(models.Model):
	class Meta:
		db_table = 'client'
	
	company = models.CharField(max_length = 255)
	name = models.CharField(max_length = 255)

# Portals	
class Portal(models.Model):
	class Meta:
		db_table = 'portal'
		
	client = models.OneToOneField(Client, related_name = 'portal')
	
# Automatically create client portal if client is new
def create_client_portal(sender, instance, created, **kwargs):
	if created:
	    portal = Portal(client = instance)
	    portal.save()
	
post_save.connect(create_client_portal, sender = Client)
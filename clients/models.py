from django.db import models
from django.db.models.signals import pre_save, post_save

# Clients		
class Client(models.Model):
	class Meta:
		db_table = 'client'
	
	company = models.CharField(max_length = 255)
	name = models.CharField(max_length = 255)
	slug = models.SlugField(max_length = 50, blank = True)

# Portals	
class Portal(models.Model):
	class Meta:
		db_table = 'portal'
		
	client = models.OneToOneField(Client, related_name = 'portal')

# Automatically generate a client slug
def create_client_slug(sender, instance, **kwargs):
	if not instance.slug:
		from slugify import slugify
		
		instance.slug = slugify(instance.company)
	
# Automatically create client portal if client is new
def create_client_portal(sender, instance, created, **kwargs):
	if created:
	    portal = Portal(client = instance)
	    portal.save()
	
pre_save.connect(create_client_slug, sender = Client)
post_save.connect(create_client_portal, sender = Client)
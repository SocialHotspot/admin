from django.db import models
from django.db.models.signals import pre_save, post_save

# Clients		
class Client(models.Model):
	class Meta:
		db_table = 'client'
	
	slug = models.SlugField(max_length = 50, blank = True)
	
	company_name = models.CharField(max_length = 255, null = True)
	contact_name = models.CharField(max_length = 255, null = True)
	
	email = models.EmailField(null = True)
	
	street = models.CharField(max_length = 100, null = True)
	number = models.IntegerField(null = True)
	city = models.CharField(max_length = 100, null = True)
	postal = models.CharField(max_length = 7, null = True)
	country = models.CharField(max_length = 2, null = True)
	
	unifi_site = models.CharField(max_length = 24, null = True)
	parent = models.ForeignKey('Client', related_name='subclients', null = True)

# Portals	
class Portal(models.Model):
	class Meta:
		db_table = 'portal'
		
	client = models.OneToOneField(Client, related_name = 'portal')
	
	logo = models.ImageField(upload_to = 'portal_images', null = True)
	
	facebook_page_id = models.BigIntegerField(null = True)
	facebook_page_username = models.CharField(max_length = 255, null = True)
	
	def facebook_enabled(self):
		return (self.facebook_page_id is not None)
	
	email_enabled = models.BooleanField(default = False)
	checkin_enabled = models.BooleanField(default = False)
	
	guest_password = models.CharField(max_length = 255, null = True)
	
	def password_enabled(self):
		return (len(self.guest_password) != 0)
		
# Hotspots		
class Hotspot(models.Model):
	class Meta:
		db_table = 'hotspot'
	
	mac_address = models.CharField(max_length = 255, null = True)
	client = models.ForeignKey('Client', related_name='hotspots', null = True)
	

# Automatically generate a client slug
def create_client_slug(sender, instance, **kwargs):
	if not instance.slug:
		from slugify import slugify
		
		instance.slug = slugify(instance.company_name)
	
# Automatically create client portal if client is new
def create_client_portal(sender, instance, created, **kwargs):
	if created:
	    portal = Portal(client = instance)
	    portal.save()
	
pre_save.connect(create_client_slug, sender = Client)
post_save.connect(create_client_portal, sender = Client)
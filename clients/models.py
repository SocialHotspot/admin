from django.db import models
from django.db.models.signals import pre_save, post_save

from django.conf import settings

import requests

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
	unifi_controller = models.ForeignKey('unifi_control.UnifiController', related_name='clients', null = True)
	
	parent = models.ForeignKey('Client', related_name='subclients', null = True)

# Portals	
class Portal(models.Model):
	class Meta:
		db_table = 'portal'
		
	client = models.OneToOneField(Client, related_name = 'portal')
	
	logo = models.ImageField(upload_to = 'logos', null = True)
	background_color = models.CharField(max_length = 7, null = True)
	
	facebook_page_id = models.BigIntegerField(null = True)
	facebook_page_username = models.CharField(max_length = 255, null = True)
	
	def facebook_enabled(self):
		return (self.facebook_page_id is not None)
	
	email_enabled = models.BooleanField(default = False)
	checkin_enabled = models.BooleanField(default = False)
	direct_access = models.BooleanField(default = False)
	
	guest_password = models.CharField(max_length = 255, null = True)

	wpa_password = models.CharField(max_length = 64, null = True)
	
	def network_password_enabled(self):
		return (self.wpa_password is not None)
	
	base_template = models.CharField(max_length = 255, null = True)
	
	def password_enabled(self):
		return (self.guest_password and len(self.guest_password) != 0)
		
	def is_liked(self, graph):
		return (len(graph.get('me/likes/'+ str(self.facebook_page_id))['data']) > 0)
		
# Portal users
class PortalUser(models.Model):
	class Meta:
		db_table = 'portal_user'
		
	portal = models.ForeignKey('Portal', related_name='users', null = False)
	
	mac_address = models.CharField(max_length = 255, null = True)
	state = models.IntegerField(default = 0, null = False)
	
	ua = models.CharField(max_length = 255, null = True)
	ip = models.CharField(max_length = 255, null = True)
	
	landed = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
		
# Hotspots		
class Hotspot(models.Model):
	class Meta:
		db_table = 'hotspot'
	
	mac_address = models.CharField(max_length = 255, null = True)
	client = models.ForeignKey('Client', related_name='hotspots', null = True)
	
	external_id = models.IntegerField(null = False, default = 1000)
	
	def get_external_info(self):
		response = requests.get(settings.CILIS_API +'/hotspot/?id='+ str(self.external_id))
		response = response.json()
		
		return response
	
	@staticmethod
	def filter_used(aps):
		existing_macs = [ hotspot.mac_address for hotspot in Hotspot.objects.all() ]
		
		return [ ap for ap in aps if ap['mac'] not in existing_macs ]
	
	@staticmethod
	def latest_id():
		latest = Hotspot.objects.order_by('-external_id').first()
		
		if latest:
			return latest.external_id
		else:
			return 1000

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
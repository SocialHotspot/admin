from django.db import models
from unifi.controller import Controller

# Unifi controller
class UnifiController(models.Model):
	class Meta:
		db_table = 'unifi_controller'
	
	host = models.CharField(max_length = 255, null = False)
	
	username = models.CharField(max_length = 255, null = False)
	password = models.CharField(max_length = 255, null = False)
	
	name = models.CharField(max_length = 10, null = True)
	stock_site = models.CharField(max_length = 32, null = True)
	
	version = models.CharField(max_length = 2, default = 'v3', null = False)
	
	def controller(self):
		return Controller(self.host, self.username, self.password, self.version, self.stock_site)
	
	@staticmethod
	def get_with_stock():
		return UnifiController.objects.exclude(stock_site = None)
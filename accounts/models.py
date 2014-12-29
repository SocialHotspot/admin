from django.db import models
from django.contrib.auth.models import User

# Admin devices		
class AdminDevice(models.Model):
	class Meta:
		db_table = 'admin_device'
	
	mac_address = models.CharField(max_length = 255)
	description = models.CharField(max_length = 255)
	
	user = models.ForeignKey(User, related_name='devices')
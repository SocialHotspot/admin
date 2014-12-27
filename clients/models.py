from django.db import models

class BaseModel(models.Model):
	class Meta:
		abstract = True
		
class Client(models.Model):
	class Meta:
		db_table = 'client'
	
	company = models.CharField(max_length = 255)
	name = models.CharField(max_length = 255)
		
	
class Portal(models.Model):
	class Meta:
		db_table = 'portal'
		
	client = models.OneToOneField(Client, related_name='portal')
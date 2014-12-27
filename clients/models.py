from django.db import models

class BaseModel(models.Model):
	class Meta:
		abstract = True
		
class Client(models.Model):
	class Meta:
		db_table = 'client'
	
	company = models.CharField(max_length = 255)
	name = models.CharField(max_length = 255)
		
	def save(self, *args, **kwargs):
		is_new = self.pk is None
		super(Client, self).save(*args, **kwargs)
		
		# Automatically create client portal if client is new
		if is_new:
		    self.portal = Portal(client=self)
		    self.portal.save()
	
class Portal(models.Model):
	class Meta:
		db_table = 'portal'
		
	client = models.OneToOneField(Client, related_name='portal')
from django.db import models
from datetime import datetime, date
from django_extensions.db.models import TimeStampedModel
from client.models import Client
# Create your models here.

class Quotation(models.Model):
	client = models.ForeignKey(Client,null=True,blank=True)
	quotation_no = models.IntegerField(unique=True)
	#created = models.DateTimeField(default=datetime.now, blank=True)
	created = models.DateField(default=date.today)
	def __unicode__(self):
		return unicode(self.client)

class Item(models.Model):
	quotation_no= models.ForeignKey(Quotation,null=True,blank=True)
	client = models.ForeignKey(Client,null=True,blank=True)
	item = models.CharField(max_length=200)
	quantity = models.IntegerField(default='0')
	price = models.FloatField()
	total = models.FloatField()
	

	def __unicode__(self):
		return self.item

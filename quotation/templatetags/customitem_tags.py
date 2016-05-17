from django import template

register = template.Library()
from quotation.models import Quotation,Item
from client.models import Client

def get_item(value):
	try:
		profile = Quotation.objects.get(quotation_no = value)
		print profile,value
		data = Item.objects.filter(quotation_no = profile)
		print data
	except:
		data = []
	return data

register.filter('get_item', get_item)


def get_client(value):
	try:
		profile = Quotation.objects.get(client = value)
		print profile,value
		data = Item.objects.filter(client = profile)
		print data
	except:
		data = []
	return data

register.filter('get_client', get_client)
from django.contrib import admin
from .models import Quotation, Item
# Register your models here.

admin.site.register(Quotation)
# admin.site.register(Item)
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	pass
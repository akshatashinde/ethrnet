from enum import Enum
from datetime import date
from django.db import models
from dateutil.relativedelta import relativedelta
from ethrnet.branch_manager import BranchWiseObjectManager
from account.models import Branch

class Supplier(models.Model):
    """
    Stock status values such as "In Stock", "Backordered", etc.
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    # eg. DLink - RK Enterprises
    code = models.CharField(max_length=255, blank=True, null=True)
    branch = models.ForeignKey(Branch, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.code:
            if self.company and self.name:
                self.code = self.company + '-' + self.name
        super(Supplier, self).save(*args, **kwargs)

    class Meta():
        verbose_name_plural = 'Suppliers'

    def __unicode__(self):
        return self.code

    objects = BranchWiseObjectManager()



class InventoryItem(models.Model):
    """
    An inventoried item represented by any Django model by means of the Content
    Types framework.
    """
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    branch = models.ForeignKey(Branch, blank=True, null=True)

    def __unicode__(self):
        return self.name

    objects = BranchWiseObjectManager()


class IteamVariation(models.Model):
    class StockStatusChoices(Enum):
        """
        This class creates enum for user_type field of UserProfile.
        """
        IN_STOCK = 'IN STOCK'
        OUT_OF_STOCK = 'OUT OF STOCK'
        ORDERED = 'ORDERED'

        @classmethod
        def as_tuple(cls):
            return ((item.value, item.name.replace('_', ' ')) for item in cls)

    status = models.CharField(blank=True, max_length=50,
                              choices=StockStatusChoices.as_tuple(),
                              default=StockStatusChoices.IN_STOCK.value
                              )
    delivered_at = models.DateField(blank=True, null=True)
    purchased_at = models.DateField(blank=True, null=True)

    inventoryitem = models.ForeignKey(InventoryItem)
    price = models.IntegerField(blank=True, null=True)
    sale_price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    # eg. Router - DLink
    code = models.CharField(max_length=255, blank=True, null=True)
    serial_no = models.CharField(max_length=255, blank=True, null=True)
    model_no = models.CharField(max_length=255, blank=True, null=True)
    warrenty_period = models.IntegerField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    supplier = models.ForeignKey(Supplier)
    branch = models.ForeignKey(Branch, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.code:
            if self.supplier.company and self.inventoryitem.name and self.model_no:
                self.code = self.supplier.company + '-' + self.inventoryitem.name + '-' + self.model_no
        if not self.expiry_date:
            if self.supplier.company:
                self.expiry_date = date.today() + relativedelta(months=+ self.warrenty_period)
        if self.quantity > 0:
            self.status = self.StockStatusChoices.IN_STOCK.value
        else:
            self.status = self.StockStatusChoices.OUT_OF_STOCK.value
        super(IteamVariation, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.code

    objects = BranchWiseObjectManager()

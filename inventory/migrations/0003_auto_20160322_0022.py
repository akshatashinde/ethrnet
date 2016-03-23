# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_iteamvariation_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iteamvariation',
            name='stock_status',
        ),
        migrations.AddField(
            model_name='iteamvariation',
            name='delivered_at',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='iteamvariation',
            name='purchased_at',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='iteamvariation',
            name='status',
            field=models.CharField(default=b'IN STOCK', max_length=50, blank=True, choices=[(b'IN STOCK', b'IN STOCK'), (b'ORDERED', b'ORDERED'), (b'OUT OF STOCK', b'OUT OF STOCK')]),
        ),
        migrations.DeleteModel(
            name='StockStatus',
        ),
    ]

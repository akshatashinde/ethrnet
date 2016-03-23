# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('quantity', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='IteamVariation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.IntegerField(null=True, blank=True)),
                ('sale_price', models.IntegerField(null=True, blank=True)),
                ('code', models.CharField(max_length=255, null=True, blank=True)),
                ('company', models.CharField(max_length=255, null=True, blank=True)),
                ('serial_no', models.CharField(max_length=255, null=True, blank=True)),
                ('warrenty_period', models.IntegerField(null=True, blank=True)),
                ('expiry_date', models.DateField(null=True, blank=True)),
                ('inventoryitem', models.ForeignKey(to='inventory.InventoryItem')),
            ],
        ),
        migrations.CreateModel(
            name='StockStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'IN STOCK', max_length=50, blank=True, choices=[(b'IN STOCK', b'IN STOCK'), (b'ORDERED', b'ORDERED'), (b'OUT OF STOCK', b'OUT OF STOCK')])),
                ('last_delivered_at', models.DateField(null=True, blank=True)),
                ('last_ordered_on', models.DateField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Stock Status',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('company', models.CharField(max_length=255, null=True, blank=True)),
                ('code', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Suppliers',
            },
        ),
        migrations.AddField(
            model_name='iteamvariation',
            name='stock_status',
            field=models.ForeignKey(to='inventory.StockStatus'),
        ),
        migrations.AddField(
            model_name='iteamvariation',
            name='supplier',
            field=models.ForeignKey(to='inventory.Supplier'),
        ),
    ]

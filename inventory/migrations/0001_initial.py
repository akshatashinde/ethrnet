# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('branch', models.ForeignKey(blank=True, to='account.Branch', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IteamVariation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'IN STOCK', max_length=50, blank=True, choices=[(b'IN STOCK', b'IN STOCK'), (b'ORDERED', b'ORDERED'), (b'OUT OF STOCK', b'OUT OF STOCK')])),
                ('delivered_at', models.DateField(null=True, blank=True)),
                ('purchased_at', models.DateField(null=True, blank=True)),
                ('price', models.IntegerField(null=True, blank=True)),
                ('sale_price', models.IntegerField(null=True, blank=True)),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('code', models.CharField(max_length=255, null=True, blank=True)),
                ('serial_no', models.CharField(max_length=255, null=True, blank=True)),
                ('model_no', models.CharField(max_length=255, null=True, blank=True)),
                ('warrenty_period', models.IntegerField(null=True, blank=True)),
                ('expiry_date', models.DateField(null=True, blank=True)),
                ('branch', models.ForeignKey(blank=True, to='account.Branch', null=True)),
                ('inventoryitem', models.ForeignKey(to='inventory.InventoryItem')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('company', models.CharField(max_length=255, null=True, blank=True)),
                ('code', models.CharField(max_length=255, null=True, blank=True)),
                ('branch', models.ForeignKey(blank=True, to='account.Branch', null=True)),
            ],
            options={
                'verbose_name_plural': 'Suppliers',
            },
        ),
        migrations.AddField(
            model_name='iteamvariation',
            name='supplier',
            field=models.ForeignKey(to='inventory.Supplier'),
        ),
    ]

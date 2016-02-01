# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=3)),
                ('pre_symbol', models.CharField(max_length=1, blank=True)),
                ('post_symbol', models.CharField(max_length=1, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('invoice_id', models.CharField(max_length=6, unique=True, null=True, editable=False, blank=True)),
                ('invoice_date', models.DateField(default=datetime.date.today)),
                ('invoiced', models.BooleanField(default=False)),
                ('draft', models.BooleanField(default=False)),
                ('paid_date', models.DateField(null=True, blank=True)),
                ('address', models.ForeignKey(related_name='invoice_set', to='account.UserAddress')),
                ('currency', models.ForeignKey(blank=True, to='invoice.Currency', null=True)),
                ('user', models.ForeignKey(to='client.Client')),
            ],
            options={
                'ordering': ('-invoice_date', 'id'),
            },
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('unit_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('quantity', models.DecimalField(default=1, max_digits=8, decimal_places=2)),
                ('invoice', models.ForeignKey(related_name='items', to='invoice.Invoice')),
            ],
        ),
    ]

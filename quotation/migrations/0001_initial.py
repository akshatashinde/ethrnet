# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_client_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateField(default=datetime.date.today)),
                ('item', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=b'0')),
                ('price', models.FloatField()),
                ('total', models.FloatField()),
                ('client', models.ForeignKey(blank=True, to='client.Client', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quotation_no', models.IntegerField(unique=True)),
                ('client', models.ForeignKey(blank=True, to='client.Client', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='quotation_no',
            field=models.ForeignKey(blank=True, to='quotation.Quotation', null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=120)),
                ('flat_no', models.CharField(max_length=120)),
                ('society', models.CharField(max_length=120)),
                ('area', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120, null=True, blank=True)),
                ('country', models.CharField(default=b'India', max_length=120)),
                ('zipcode', models.CharField(max_length=25)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated', '-timestamp'],
            },
        ),
    ]

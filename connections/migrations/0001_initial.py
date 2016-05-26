# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160329_0021'),
        ('client', '0003_client_is_active'),
        ('plans', '0002_auto_20160329_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('expired_on', models.DateField()),
                ('branch', models.ForeignKey(blank=True, to='account.Branch', null=True)),
                ('client', models.ForeignKey(to='client.Client')),
                ('plan', models.ForeignKey(to='plans.Plans')),
            ],
        ),
        migrations.CreateModel(
            name='ConnectionHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField()),
                ('updated_on', models.DateTimeField()),
                ('expired_on', models.DateField()),
                ('branch', models.ForeignKey(blank=True, to='account.Branch', null=True)),
                ('client', models.ForeignKey(to='client.Client')),
                ('plan', models.ForeignKey(to='plans.Plans')),
            ],
        ),
    ]

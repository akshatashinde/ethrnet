# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plan_type', models.CharField(max_length=20, null=True, choices=[(b'Commertial', b'COMMERTIAL'), (b'Personal', b'PERSONAL')])),
                ('price', models.FloatField()),
                ('duration', models.IntegerField()),
                ('download_speed', models.IntegerField()),
                ('FUP_limit', models.IntegerField()),
                ('post_FUP_speed', models.IntegerField()),
                ('installation_charges', models.IntegerField()),
                ('subscription_amount', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]

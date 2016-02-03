# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_auto_20160201_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('landmark', models.CharField(max_length=255, null=True, blank=True)),
                ('birth_date', models.DateTimeField()),
                ('gender', models.CharField(max_length=20, null=True, choices=[(b'Female', b'FEMALE'), (b'Male', b'MALE'), (b'Others', b'OTHERS')])),
                ('id_proof_types', models.CharField(max_length=20, null=True, choices=[(b'Aadhar', b'AADHAR'), (b'Driving Licence', b'DRIVING LICENCE'), (b'PAN', b'PAN'), (b'Passport', b'PASSPORT'), (b'Voter', b'VOTER')])),
                ('id_proof', models.ImageField(upload_to=b'')),
                ('address_proof_types', models.CharField(max_length=20, null=True, choices=[(b'Aadhar', b'AADHAR'), (b'Driving Licence', b'DRIVING LICENCE'), (b'Electricity Bill', b'ELECTRICITY BILL'), (b'Passport', b'PASSPORT'), (b'Voter', b'VOTER')])),
                ('address_proof', models.ImageField(upload_to=b'')),
                ('is_active', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('expired_on', models.DateTimeField()),
                ('plan', models.ForeignKey(to='plans.Plans')),
            ],
        ),
    ]

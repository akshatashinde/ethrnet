# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('fileupload', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('client_id', models.CharField(max_length=250, null=True, blank=True)),
                ('email', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(default=b'Other', max_length=20, null=True, choices=[(b'Female', b'FEMALE'), (b'Male', b'MALE'), (b'Other', b'OTHER')])),
                ('id_proof_types', models.CharField(default=b'Other', max_length=20, null=True, blank=True, choices=[(b'Aadhar', b'AADHAR'), (b'Driving Licence', b'DRIVING LICENCE'), (b'Other', b'OTHER'), (b'PAN', b'PAN'), (b'Passport', b'PASSPORT'), (b'Voter', b'VOTER')])),
                ('address_proof_types', models.CharField(default=b'Other', max_length=20, null=True, blank=True, choices=[(b'Aadhar', b'AADHAR'), (b'Driving Licence', b'DRIVING LICENCE'), (b'Electricity Bill', b'ELECTRICITY BILL'), (b'Other', b'OTHER'), (b'Passport', b'PASSPORT'), (b'Voter', b'VOTER')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('Address', models.ForeignKey(blank=True, to='account.UserAddress', null=True)),
                ('attachments', models.ManyToManyField(to='fileupload.Picture', null=True, blank=True)),
                ('branch', models.ForeignKey(blank=True, to='account.Branch', null=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unifi_control', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(blank=True)),
                ('company_name', models.CharField(max_length=255, null=True)),
                ('contact_name', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=75, null=True)),
                ('street', models.CharField(max_length=100, null=True)),
                ('number', models.IntegerField(null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('postal', models.CharField(max_length=7, null=True)),
                ('country', models.CharField(max_length=2, null=True)),
                ('unifi_site', models.CharField(max_length=24, null=True)),
                ('parent', models.ForeignKey(related_name=b'subclients', to='clients.Client', null=True)),
                ('unifi_controller', models.ForeignKey(related_name=b'clients', to='unifi_control.UnifiController', null=True)),
            ],
            options={
                'db_table': 'client',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hotspot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac_address', models.CharField(max_length=255, null=True)),
                ('external_id', models.IntegerField(default=1000)),
                ('client', models.ForeignKey(related_name=b'hotspots', to='clients.Client', null=True)),
            ],
            options={
                'db_table': 'hotspot',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('logo', models.ImageField(null=True, upload_to=b'logos')),
                ('background_color', models.CharField(max_length=7, null=True)),
                ('facebook_page_id', models.BigIntegerField(null=True)),
                ('facebook_page_username', models.CharField(max_length=255, null=True)),
                ('email_enabled', models.BooleanField(default=False)),
                ('checkin_enabled', models.BooleanField(default=False)),
                ('direct_access', models.BooleanField(default=False)),
                ('guest_password', models.CharField(max_length=255, null=True)),
                ('wpa_password', models.CharField(max_length=64, null=True)),
                ('base_template', models.CharField(max_length=255, null=True)),
                ('client', models.OneToOneField(related_name=b'portal', to='clients.Client')),
            ],
            options={
                'db_table': 'portal',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PortalUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac_address', models.CharField(max_length=255, null=True)),
                ('state', models.IntegerField(default=0)),
                ('ua', models.CharField(max_length=255, null=True)),
                ('ip', models.CharField(max_length=255, null=True)),
                ('landed', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('portal', models.ForeignKey(related_name=b'users', to='clients.Portal')),
            ],
            options={
                'db_table': 'portal_user',
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Portal.wpa_password'
        db.add_column('portal', 'wpa_password',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True),
                      keep_default=False)

        # Deleting field 'Hotspot.wpa_password'
        db.delete_column('hotspot', 'wpa_password')


    def backwards(self, orm):
        # Deleting field 'Portal.wpa_password'
        db.delete_column('portal', 'wpa_password')

        # Adding field 'Hotspot.wpa_password'
        db.add_column('hotspot', 'wpa_password',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True),
                      keep_default=False)


    models = {
        u'clients.client': {
            'Meta': {'object_name': 'Client', 'db_table': "'client'"},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subclients'", 'null': 'True', 'to': u"orm['clients.Client']"}),
            'postal': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'unifi_controller': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clients'", 'null': 'True', 'to': u"orm['unifi_control.UnifiController']"}),
            'unifi_site': ('django.db.models.fields.CharField', [], {'max_length': '24', 'null': 'True'})
        },
        u'clients.hotspot': {
            'Meta': {'object_name': 'Hotspot', 'db_table': "'hotspot'"},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hotspots'", 'null': 'True', 'to': u"orm['clients.Client']"}),
            'external_id': ('django.db.models.fields.IntegerField', [], {'default': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mac_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        u'clients.portal': {
            'Meta': {'object_name': 'Portal', 'db_table': "'portal'"},
            'base_template': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'checkin_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'client': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'portal'", 'unique': 'True', 'to': u"orm['clients.Client']"}),
            'direct_access': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'facebook_page_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'facebook_page_username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'guest_password': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'wpa_password': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'})
        },
        u'clients.portaluser': {
            'Meta': {'object_name': 'PortalUser', 'db_table': "'portal_user'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'landed': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'mac_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'portal': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'users'", 'to': u"orm['clients.Portal']"}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ua': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'unifi_control.unificontroller': {
            'Meta': {'object_name': 'UnifiController', 'db_table': "'unifi_controller'"},
            'host': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'stock_site': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'v3'", 'max_length': '2'})
        }
    }

    complete_apps = ['clients']
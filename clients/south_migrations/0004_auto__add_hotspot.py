# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hotspot'
        db.create_table('hotspot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mac_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(related_name='hotspots', null=True, to=orm['clients.Client'])),
        ))
        db.send_create_signal(u'clients', ['Hotspot'])


    def backwards(self, orm):
        # Deleting model 'Hotspot'
        db.delete_table('hotspot')


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
            'unifi_site': ('django.db.models.fields.CharField', [], {'max_length': '24', 'null': 'True'})
        },
        u'clients.hotspot': {
            'Meta': {'object_name': 'Hotspot', 'db_table': "'hotspot'"},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hotspots'", 'null': 'True', 'to': u"orm['clients.Client']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mac_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        u'clients.portal': {
            'Meta': {'object_name': 'Portal', 'db_table': "'portal'"},
            'checkin_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'client': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'portal'", 'unique': 'True', 'to': u"orm['clients.Client']"}),
            'email_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'facebook_page_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'facebook_page_username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'guest_password': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'})
        }
    }

    complete_apps = ['clients']
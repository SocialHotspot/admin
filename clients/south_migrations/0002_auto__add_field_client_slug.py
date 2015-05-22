# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Client.slug'
        db.add_column('client', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=50, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Client.slug'
        db.delete_column('client', 'slug')


    models = {
        u'clients.client': {
            'Meta': {'object_name': 'Client', 'db_table': "'client'"},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'clients.portal': {
            'Meta': {'object_name': 'Portal', 'db_table': "'portal'"},
            'client': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'portal'", 'unique': 'True', 'to': u"orm['clients.Client']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['clients']
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Client'
        db.create_table('client', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'clients', ['Client'])

        # Adding model 'Portal'
        db.create_table('portal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.OneToOneField')(related_name='portal', unique=True, to=orm['clients.Client'])),
        ))
        db.send_create_signal(u'clients', ['Portal'])


    def backwards(self, orm):
        # Deleting model 'Client'
        db.delete_table('client')

        # Deleting model 'Portal'
        db.delete_table('portal')


    models = {
        u'clients.client': {
            'Meta': {'object_name': 'Client', 'db_table': "'client'"},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'clients.portal': {
            'Meta': {'object_name': 'Portal', 'db_table': "'portal'"},
            'client': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'portal'", 'unique': 'True', 'to': u"orm['clients.Client']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['clients']
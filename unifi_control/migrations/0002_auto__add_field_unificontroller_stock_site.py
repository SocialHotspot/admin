# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UnifiController.stock_site'
        db.add_column('unifi_controller', 'stock_site',
                      self.gf('django.db.models.fields.CharField')(max_length=32, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UnifiController.stock_site'
        db.delete_column('unifi_controller', 'stock_site')


    models = {
        u'unifi_control.unificontroller': {
            'Meta': {'object_name': 'UnifiController', 'db_table': "'unifi_controller'"},
            'host': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'stock_site': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['unifi_control']
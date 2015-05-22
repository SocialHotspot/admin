# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Client.company'
        db.delete_column('client', 'company')

        # Deleting field 'Client.name'
        db.delete_column('client', 'name')

        # Adding field 'Client.company_name'
        db.add_column('client', 'company_name',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)

        # Adding field 'Client.contact_name'
        db.add_column('client', 'contact_name',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)

        # Adding field 'Client.email'
        db.add_column('client', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=75, null=True),
                      keep_default=False)

        # Adding field 'Client.street'
        db.add_column('client', 'street',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Client.number'
        db.add_column('client', 'number',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Client.city'
        db.add_column('client', 'city',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Client.postal'
        db.add_column('client', 'postal',
                      self.gf('django.db.models.fields.CharField')(max_length=7, null=True),
                      keep_default=False)

        # Adding field 'Client.country'
        db.add_column('client', 'country',
                      self.gf('django.db.models.fields.CharField')(max_length=2, null=True),
                      keep_default=False)

        # Adding field 'Client.unifi_site'
        db.add_column('client', 'unifi_site',
                      self.gf('django.db.models.fields.CharField')(max_length=24, null=True),
                      keep_default=False)

        # Adding field 'Client.parent'
        db.add_column('client', 'parent',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='subclients', null=True, to=orm['clients.Client']),
                      keep_default=False)

        # Adding field 'Portal.logo'
        db.add_column('portal', 'logo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Portal.facebook_page_id'
        db.add_column('portal', 'facebook_page_id',
                      self.gf('django.db.models.fields.BigIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Portal.facebook_page_username'
        db.add_column('portal', 'facebook_page_username',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)

        # Adding field 'Portal.guest_password'
        db.add_column('portal', 'guest_password',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)

        # Adding field 'Portal.email_enabled'
        db.add_column('portal', 'email_enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Portal.checkin_enabled'
        db.add_column('portal', 'checkin_enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Client.company'
        raise RuntimeError("Cannot reverse this migration. 'Client.company' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Client.company'
        db.add_column('client', 'company',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Client.name'
        raise RuntimeError("Cannot reverse this migration. 'Client.name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Client.name'
        db.add_column('client', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)

        # Deleting field 'Client.company_name'
        db.delete_column('client', 'company_name')

        # Deleting field 'Client.contact_name'
        db.delete_column('client', 'contact_name')

        # Deleting field 'Client.email'
        db.delete_column('client', 'email')

        # Deleting field 'Client.street'
        db.delete_column('client', 'street')

        # Deleting field 'Client.number'
        db.delete_column('client', 'number')

        # Deleting field 'Client.city'
        db.delete_column('client', 'city')

        # Deleting field 'Client.postal'
        db.delete_column('client', 'postal')

        # Deleting field 'Client.country'
        db.delete_column('client', 'country')

        # Deleting field 'Client.unifi_site'
        db.delete_column('client', 'unifi_site')

        # Deleting field 'Client.parent'
        db.delete_column('client', 'parent_id')

        # Deleting field 'Portal.logo'
        db.delete_column('portal', 'logo')

        # Deleting field 'Portal.facebook_page_id'
        db.delete_column('portal', 'facebook_page_id')

        # Deleting field 'Portal.facebook_page_username'
        db.delete_column('portal', 'facebook_page_username')

        # Deleting field 'Portal.guest_password'
        db.delete_column('portal', 'guest_password')

        # Deleting field 'Portal.email_enabled'
        db.delete_column('portal', 'email_enabled')

        # Deleting field 'Portal.checkin_enabled'
        db.delete_column('portal', 'checkin_enabled')


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
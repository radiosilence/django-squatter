# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TenantMapping'
        db.create_table(u'squatter_tenantmapping', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], unique=True)),
            ('tenant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['squatter.Tenant'])),
        ))
        db.send_create_signal(u'squatter', ['TenantMapping'])

        # Adding model 'Tenant'
        db.create_table(u'squatter_tenant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('database_engine', self.gf('django.db.models.fields.CharField')(default='django.db.backends.postgresql_psycopg2', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('database_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('database_host', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('database_port', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('database_user', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('database_password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('database_options', self.gf('django.db.models.fields.TextField')(default='{}')),
        ))
        db.send_create_signal(u'squatter', ['Tenant'])


    def backwards(self, orm):
        
        # Deleting model 'TenantMapping'
        db.delete_table(u'squatter_tenantmapping')

        # Deleting model 'Tenant'
        db.delete_table(u'squatter_tenant')


    models = {
        u'sites.site': {
            'Meta': {'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'squatter.tenant': {
            'Meta': {'object_name': 'Tenant'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'database_engine': ('django.db.models.fields.CharField', [], {'default': "'django.db.backends.postgresql_psycopg2'", 'max_length': '255'}),
            'database_host': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'database_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'database_options': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'database_password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'database_port': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'database_user': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tenants'", 'symmetrical': 'False', 'through': u"orm['squatter.TenantMapping']", 'to': u"orm['sites.Site']"})
        },
        u'squatter.tenantmapping': {
            'Meta': {'object_name': 'TenantMapping'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'unique': 'True'}),
            'tenant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['squatter.Tenant']"})
        }
    }

    complete_apps = ['squatter']

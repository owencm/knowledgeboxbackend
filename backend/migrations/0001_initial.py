# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'User'
        db.create_table(u'backend_user', (
            ('username', self.gf('django.db.models.fields.CharField')(max_length=20)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'backend', ['User'])

        # Adding model 'QaItem'
        db.create_table(u'backend_qaitem', (
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=400)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.User'])),
        ))
        db.send_create_signal(u'backend', ['QaItem'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'User'
        db.delete_table(u'backend_user')

        # Deleting model 'QaItem'
        db.delete_table(u'backend_qaitem')
    
    
    models = {
        u'backend.qaitem': {
            'Meta': {'object_name': 'QaItem'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        u'backend.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }
    
    complete_apps = ['backend']

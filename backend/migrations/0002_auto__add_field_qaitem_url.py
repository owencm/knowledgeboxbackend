# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'QaItem.url'
        db.add_column(u'backend_qaitem', 'url', self.gf('django.db.models.fields.CharField')(default='http://www.google.com/', max_length=400), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting field 'QaItem.url'
        db.delete_column(u'backend_qaitem', 'url')
    
    
    models = {
        u'backend.qaitem': {
            'Meta': {'object_name': 'QaItem'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        u'backend.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }
    
    complete_apps = ['backend']

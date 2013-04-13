# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Learning'
        db.create_table(u'backend_learning', (
            ('qaitem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.QaItem'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.User'])),
        ))
        db.send_create_signal(u'backend', ['Learning'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Learning'
        db.delete_table(u'backend_learning')
    
    
    models = {
        u'backend.learning': {
            'Meta': {'object_name': 'Learning'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'qaitem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.QaItem']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.User']"})
        },
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

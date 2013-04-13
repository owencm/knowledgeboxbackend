# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Deleting model 'Learning'
        db.delete_table(u'backend_learning')

        # Adding M2M table for field learners on 'QaItem'
        db.create_table(u'backend_qaitem_learners', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('qaitem', models.ForeignKey(orm[u'backend.qaitem'], null=False)),
            ('user', models.ForeignKey(orm[u'backend.user'], null=False))
        ))
        db.create_unique(u'backend_qaitem_learners', ['qaitem_id', 'user_id'])
    
    
    def backwards(self, orm):
        
        # Adding model 'Learning'
        db.create_table(u'backend_learning', (
            ('qaitem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.QaItem'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.User'])),
        ))
        db.send_create_signal(u'backend', ['Learning'])

        # Removing M2M table for field learners on 'QaItem'
        db.delete_table('backend_qaitem_learners')
    
    
    models = {
        u'backend.qaitem': {
            'Meta': {'object_name': 'QaItem'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owner'", 'to': u"orm['backend.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'learners': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['backend.User']", 'symmetrical': 'False'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        u'backend.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }
    
    complete_apps = ['backend']

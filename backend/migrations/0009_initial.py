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
            ('password', self.gf('django.db.models.fields.CharField')(max_length=40)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'backend', ['User'])

        # Adding model 'QaItem'
        db.create_table(u'backend_qaitem', (
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='owner', to=orm['backend.User'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=400)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'backend', ['QaItem'])

        # Adding M2M table for field learners on 'QaItem'
        db.create_table(u'backend_qaitem_learners', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('qaitem', models.ForeignKey(orm[u'backend.qaitem'], null=False)),
            ('user', models.ForeignKey(orm[u'backend.user'], null=False))
        ))
        db.create_unique(u'backend_qaitem_learners', ['qaitem_id', 'user_id'])

        # Adding model 'QResponse'
        db.create_table(u'backend_qresponse', (
            ('answered_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('qid', self.gf('django.db.models.fields.related.ForeignKey')(related_name='qaitem', to=orm['backend.QaItem'])),
            ('userid', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user', to=orm['backend.User'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('correct', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal(u'backend', ['QResponse'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'User'
        db.delete_table(u'backend_user')

        # Deleting model 'QaItem'
        db.delete_table(u'backend_qaitem')

        # Removing M2M table for field learners on 'QaItem'
        db.delete_table('backend_qaitem_learners')

        # Deleting model 'QResponse'
        db.delete_table(u'backend_qresponse')
    
    
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
        u'backend.qresponse': {
            'Meta': {'object_name': 'QResponse'},
            'answered_at': ('django.db.models.fields.DateTimeField', [], {}),
            'correct': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'qid': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'qaitem'", 'to': u"orm['backend.QaItem']"}),
            'userid': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user'", 'to': u"orm['backend.User']"})
        },
        u'backend.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }
    
    complete_apps = ['backend']

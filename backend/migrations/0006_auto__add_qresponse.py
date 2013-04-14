# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'QResponse'
        db.create_table(u'backend_qresponse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('qid', self.gf('django.db.models.fields.related.ForeignKey')(related_name='qaitem', to=orm['backend.QaItem'])),
            ('userid', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user', to=orm['backend.User'])),
            ('correct', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('answered_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'backend', ['QResponse'])


    def backwards(self, orm):
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
            'correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
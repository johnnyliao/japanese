# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AWS'
        db.create_table(u'news_aws', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('s_key', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'news', ['AWS'])


    def backwards(self, orm):
        # Deleting model 'AWS'
        db.delete_table(u'news_aws')


    models = {
        u'news.aws': {
            'Meta': {'object_name': 'AWS'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            's_key': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'news.news': {
            'Meta': {'object_name': 'News'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '8000'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'news_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pubdate': ('django.db.models.fields.DateTimeField', [], {}),
            'rev': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'news.newsaudio': {
            'Meta': {'object_name': 'NewsAudio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'news_video'", 'unique': 'True', 'null': 'True', 'to': u"orm['news.News']"}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'news.newsphoto': {
            'Meta': {'object_name': 'NewsPhoto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'news_photo'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['news.News']"}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['news']
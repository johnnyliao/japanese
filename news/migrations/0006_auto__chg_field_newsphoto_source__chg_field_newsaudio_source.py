# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'NewsPhoto.source'
        db.alter_column(u'news_newsphoto', 'source', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'NewsAudio.source'
        db.alter_column(u'news_newsaudio', 'source', self.gf('django.db.models.fields.CharField')(max_length=400))

    def backwards(self, orm):

        # Changing field 'NewsPhoto.source'
        db.alter_column(u'news_newsphoto', 'source', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'NewsAudio.source'
        db.alter_column(u'news_newsaudio', 'source', self.gf('django.db.models.fields.CharField')(max_length=100))

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
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        u'news.newsphoto': {
            'Meta': {'object_name': 'NewsPhoto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'news_photo'", 'unique': 'True', 'null': 'True', 'to': u"orm['news.News']"}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        }
    }

    complete_apps = ['news']
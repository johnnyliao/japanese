# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NewsPhoto.news'
        db.add_column(u'news_newsphoto', 'news',
                      self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='news_photo', unique=True, null=True, to=orm['news.News']),
                      keep_default=False)

        # Adding field 'NewsPhoto.source'
        db.add_column(u'news_newsphoto', 'source',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Removing M2M table for field news on 'NewsPhoto'
        db.delete_table(db.shorten_name(u'news_newsphoto_news'))


    def backwards(self, orm):
        # Deleting field 'NewsPhoto.news'
        db.delete_column(u'news_newsphoto', 'news_id')

        # Deleting field 'NewsPhoto.source'
        db.delete_column(u'news_newsphoto', 'source')

        # Adding M2M table for field news on 'NewsPhoto'
        m2m_table_name = db.shorten_name(u'news_newsphoto_news')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsphoto', models.ForeignKey(orm[u'news.newsphoto'], null=False)),
            ('news', models.ForeignKey(orm[u'news.news'], null=False))
        ))
        db.create_unique(m2m_table_name, ['newsphoto_id', 'news_id'])


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
            'source': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'news.newsphoto': {
            'Meta': {'object_name': 'NewsPhoto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'news_photo'", 'unique': 'True', 'null': 'True', 'to': u"orm['news.News']"}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['news']
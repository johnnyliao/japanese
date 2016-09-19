# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'News'
        db.create_table(u'news_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('news_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rev', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=4096)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=4096)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('pubdate', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'news', ['News'])


    def backwards(self, orm):
        # Deleting model 'News'
        db.delete_table(u'news_news')


    models = {
        u'news.news': {
            'Meta': {'object_name': 'News'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'news_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pubdate': ('django.db.models.fields.DateTimeField', [], {}),
            'rev': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['news']
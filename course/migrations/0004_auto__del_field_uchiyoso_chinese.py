# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'UChiYoSo.chinese'
        db.delete_column(u'course_uchiyoso', 'chinese')


    def backwards(self, orm):
        # Adding field 'UChiYoSo.chinese'
        db.add_column(u'course_uchiyoso', 'chinese',
                      self.gf('django.db.models.fields.CharField')(default=True, max_length=30),
                      keep_default=False)


    models = {
        u'course.uchiyoso': {
            'Meta': {'object_name': 'UChiYoSo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kana': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'kanji': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'course.verb': {
            'Meta': {'object_name': 'Verb'},
            'chinese': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kana': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'kanji': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'uchi': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'verb_uchi'", 'unique': 'True', 'null': 'True', 'to': u"orm['course.UChiYoSo']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'yoso': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'verb_yoso'", 'unique': 'True', 'null': 'True', 'to': u"orm['course.UChiYoSo']"})
        },
        u'course.word': {
            'Meta': {'object_name': 'Word'},
            'chinese': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kana': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'kanji': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'uchi': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'word_uchi'", 'unique': 'True', 'null': 'True', 'to': u"orm['course.UChiYoSo']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'yoso': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'word_yoso'", 'unique': 'True', 'null': 'True', 'to': u"orm['course.UChiYoSo']"})
        }
    }

    complete_apps = ['course']
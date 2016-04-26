# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UChiYoSo'
        db.create_table(u'course_uchiyoso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kanji', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('kana', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('chinese', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'course', ['UChiYoSo'])

        # Adding field 'Word.uchi'
        db.add_column(u'course_word', 'uchi',
                      self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='word_uchi', unique=True, null=True, to=orm['course.UChiYoSo']),
                      keep_default=False)

        # Adding field 'Word.yoso'
        db.add_column(u'course_word', 'yoso',
                      self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='word_yoso', unique=True, null=True, to=orm['course.UChiYoSo']),
                      keep_default=False)

        # Adding field 'Verb.uchi'
        db.add_column(u'course_verb', 'uchi',
                      self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='verb_uchi', unique=True, null=True, to=orm['course.UChiYoSo']),
                      keep_default=False)

        # Adding field 'Verb.yoso'
        db.add_column(u'course_verb', 'yoso',
                      self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='verb_yoso', unique=True, null=True, to=orm['course.UChiYoSo']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'UChiYoSo'
        db.delete_table(u'course_uchiyoso')

        # Deleting field 'Word.uchi'
        db.delete_column(u'course_word', 'uchi_id')

        # Deleting field 'Word.yoso'
        db.delete_column(u'course_word', 'yoso_id')

        # Deleting field 'Verb.uchi'
        db.delete_column(u'course_verb', 'uchi_id')

        # Deleting field 'Verb.yoso'
        db.delete_column(u'course_verb', 'yoso_id')


    models = {
        u'course.uchiyoso': {
            'Meta': {'object_name': 'UChiYoSo'},
            'chinese': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
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
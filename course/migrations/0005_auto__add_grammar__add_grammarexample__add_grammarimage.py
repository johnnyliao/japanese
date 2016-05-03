# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Grammar'
        db.create_table(u'course_grammar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'course', ['Grammar'])

        # Adding model 'GrammarExample'
        db.create_table(u'course_grammarexample', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grammar', self.gf('django.db.models.fields.related.ForeignKey')(related_name='grammar_example', to=orm['course.Grammar'])),
            ('example', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'course', ['GrammarExample'])

        # Adding model 'GrammarImage'
        db.create_table(u'course_grammarimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grammar', self.gf('django.db.models.fields.related.ForeignKey')(related_name='grammar_image', to=orm['course.Grammar'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'course', ['GrammarImage'])


    def backwards(self, orm):
        # Deleting model 'Grammar'
        db.delete_table(u'course_grammar')

        # Deleting model 'GrammarExample'
        db.delete_table(u'course_grammarexample')

        # Deleting model 'GrammarImage'
        db.delete_table(u'course_grammarimage')


    models = {
        u'course.grammar': {
            'Meta': {'object_name': 'Grammar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'course.grammarexample': {
            'Meta': {'object_name': 'GrammarExample'},
            'example': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'grammar': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'grammar_example'", 'to': u"orm['course.Grammar']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'course.grammarimage': {
            'Meta': {'object_name': 'GrammarImage'},
            'grammar': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'grammar_image'", 'to': u"orm['course.Grammar']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
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
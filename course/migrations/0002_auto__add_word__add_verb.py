# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Word'
        db.create_table(u'course_word', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kanji', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('kana', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('chinese', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('level', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'course', ['Word'])

        # Adding model 'Verb'
        db.create_table(u'course_verb', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kanji', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('kana', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('chinese', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('level', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('group', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'course', ['Verb'])


    def backwards(self, orm):
        # Deleting model 'Word'
        db.delete_table(u'course_word')

        # Deleting model 'Verb'
        db.delete_table(u'course_verb')


    models = {
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
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
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
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['course']
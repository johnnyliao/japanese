#-*- encoding: utf-8 -*-
from django import forms

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin, UserChangeForm as DjangoUserChangeForm
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from course.models import *
from salmonella.admin import SalmonellaMixin
from django.utils.translation import ugettext_lazy as _

class UChiYoSoAdmin(SalmonellaMixin, admin.ModelAdmin):
    list_display = ["kana", "kanji"]
    search_fields = ["kanji", "kana"]

class VerbAdmin(SalmonellaMixin, admin.ModelAdmin):
    list_display = ["kana", "kanji", "chinese", "group", "type", "level", "number"]
    search_fields = ["kanji", "kana", "chinese"]
    list_filter = ["group", "type", "level", "number"]
    salmonella_fields  = ["uchi", "yoso"]

class WordAdmin(SalmonellaMixin, admin.ModelAdmin):
    list_display = ["kana", "kanji", "chinese", "type", "level", "number"]
    search_fields = ["kanji", "kana", "chinese"]
    list_filter = ["type", "level", "number"]
    salmonella_fields  = ["uchi", "yoso"]

class GrammarAdmin(SalmonellaMixin, admin.ModelAdmin):
    list_display = ["title", "chinese", "level", "number"]
    search_fields = ["title", "chinese"]
    list_filter = ["level", "number"]

class GrammarExampleAdmin(SalmonellaMixin, admin.ModelAdmin):
    list_display = ["example"]
    salmonella_fields  = ["grammar"]

class GrammarImageAdmin(SalmonellaMixin, admin.ModelAdmin):
    list_display = ["image_tag", "image"]
    salmonella_fields  = ["grammar"]


admin.site.register(Word, WordAdmin)
admin.site.register(Verb, VerbAdmin)
admin.site.register(UChiYoSo, UChiYoSoAdmin)
admin.site.register(Grammar, GrammarAdmin)
admin.site.register(GrammarExample, GrammarExampleAdmin)
admin.site.register(GrammarImage, GrammarImageAdmin)


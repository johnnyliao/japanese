#-*- encoding: utf-8 -*-
from django import forms

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin, UserChangeForm as DjangoUserChangeForm
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from course.models import *
from salmonella.admin import SalmonellaMixin
from django.utils.translation import ugettext_lazy as _

class VerbAdmin(SalmonellaMixin, admin.ModelAdmin):
    list_display = ["kanji", "kana", "chinese", "group", "type", "level", "number"]
    search_fields = ["kanji", "kana", "chinese"]
    list_filter = ["group", "type", "level", "number"]

class WordAdmin(SalmonellaMixin, admin.ModelAdmin):
    list_display = ["kanji", "kana", "chinese", "type", "level", "number"]
    search_fields = ["kanji", "kana", "chinese"]
    list_filter = ["type", "level", "number"]

admin.site.register(Word, WordAdmin)
admin.site.register(Verb, VerbAdmin)


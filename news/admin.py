#-*- encoding: utf-8 -*-
from django import forms

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin, UserChangeForm as DjangoUserChangeForm
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from news.models import *
from salmonella.admin import SalmonellaMixin
from django.utils.translation import ugettext_lazy as _


class NewsAdmin(SalmonellaMixin, admin.ModelAdmin):
    list_display = ["news_id", "rev", "title", "pubdate", "updated"]
    search_fields = ["title", "content"]
    list_filter = ["pubdate"]
    #salmonella_fields  = ["uchi", "yoso"]

class NewsAudioAdmin(SalmonellaMixin, admin.ModelAdmin):
    list_display = ["news", "path"]


admin.site.register(News, NewsAdmin)
admin.site.register(NewsAudio, NewsAudioAdmin)


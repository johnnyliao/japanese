#-*- encoding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.contenttypes import generic
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sites.models import Site
import urlparse, settings
from django.utils import simplejson
from datetime import datetime

class News(models.Model):
	news_id = models.CharField(_(u"id編號"), max_length=50)
	rev = models.CharField(_(u"rev"), max_length=50)
	content = models.CharField(_(u"內容"), max_length=8000)
	description = models.CharField(_(u"敘述"), max_length=4096)
	title = models.CharField(_(u"title"), max_length=1024)
	link = models.CharField(_(u"原始連結"), max_length=1024)
	updated = models.DateTimeField(_(u"更新時間"), auto_now_add=True)
	pubdate = models.DateTimeField(_(u"新聞時間"))

	def save(self, *args, **kwargs):
		self.updated = datetime.now()
		return super(News, self).save(*args, **kwargs)

class NewsAudio(models.Model):
	path = models.CharField(_(u"s3路徑"), max_length=1024)
	news = models.OneToOneField('News', related_name='news_video', blank=True, null=True, verbose_name=_(u"新聞"))

class NewsPhoto(models.Model):
	path = models.CharField(_(u"s3路徑"), max_length=1024)
	news = models.ManyToManyField('News', related_name='news_photo', blank=True, null=True, verbose_name=_(u"新聞"))

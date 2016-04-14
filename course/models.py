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

TYPE_CHOICES = (
	("noun", u'名詞'),
	("adj", u'形容詞'),
	("time", u'時數詞'),
	("sulu_noun", u'する名詞'),
	("na_noun", u'なにで名詞'),
)

LEVEL_CHOICES = (
	("J1", u'J1'),
	("J2", u'J2'),
	("J3", u'J3'),
	("J4", u'J4'),
	("J5", u'J5'),
	("J6", u'J6'),
	("J7", u'J7'),
)

GROUP_CHOICES = (
	("1", u'1'),
	("2", u'2'),
	("3", u'3'),
)

VERB_TYPE_CHOICES = (
	("1", u'1'),
	("2", u'2'),
	("3", u'3'),
)

class WordBase(models.Model):
	kanji = models.CharField(_(u"漢字"), max_length=30, blank=True, null=True)
	kana = models.CharField(_(u"假名"), max_length=30)
	chinese = models.CharField(_(u"解釋"), max_length=30)
	level = models.CharField(_(u"課程等級"), max_length=10, choices=LEVEL_CHOICES)
	number = models.IntegerField(_(u"第幾天"))
	updated = models.DateTimeField(_(u"更新時間"), auto_now_add=True)

	def save(self, *args, **kwargs):
		self.updated = datetime.now()
		return super(WordBase, self).save(*args, **kwargs)

	class Meta:
	  	abstract = True

class Word(WordBase):
	type = models.CharField(_(u"類型"), max_length=20, choices=TYPE_CHOICES)

	class Meta:
		verbose_name = _(u"單字")
	  	verbose_name_plural = _(u"單字列表")

#動詞
class Verb(WordBase):
	group = models.CharField(_(u"Group"), max_length=5, choices=GROUP_CHOICES)
	type = models.CharField(_(u"Type"), max_length=5, choices=VERB_TYPE_CHOICES)

	class Meta:
		verbose_name = _(u"動詞")
	  	verbose_name_plural = _(u"動詞列表")

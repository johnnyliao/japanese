#-*- encoding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from news.models import News

from rest_framework import serializers

from datetime import datetime,timedelta
from django.utils import timezone
import urlparse
from django.contrib.sites.models import Site
from news.models import News, NewsPhoto, NewsAudio
from django.core.exceptions import ObjectDoesNotExist

class NewsSerializers(serializers.ModelSerializer):

	class Meta:
		model = News

class NewsPhotoSerializers(serializers.ModelSerializer):

	class Meta:
		model = NewsPhoto

class NewsListSerializers(serializers.ModelSerializer):
	photo = serializers.SerializerMethodField('get_photo_info')

	class Meta:
		model = News
		exclude = ('rev', 'content', 'description', 'link', 'updated')

	def get_photo_info(self, obj):
		try:
			news_photo = NewsPhoto.objects.get(news=obj)
			serializer = NewsPhotoSerializers(news_photo)
			return serializer.data["path"]
		except ObjectDoesNotExist:
			return

class GetNewsSerializers(serializers.Serializer):
	start = serializers.IntegerField(required=False)
	limit = serializers.IntegerField(required=False)

class AddCollectNewsSerializers(serializers.Serializer):
	news_id = serializers.IntegerField()

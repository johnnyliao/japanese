#-*- encoding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from course.models import Word, Verb, UChiYoSo

from rest_framework import serializers

from datetime import datetime,timedelta
from django.utils import timezone
import urlparse
from django.contrib.sites.models import Site

class GetStartLimitDataSerializer(serializers.Serializer):
    start = serializers.IntegerField(required=False)
    limit = serializers.IntegerField(required=False)

class UChiYoSoSerializer(serializers.ModelSerializer):

	class Meta:
		model = UChiYoSo

class GetWordSerializer(serializers.ModelSerializer):
	display_type = serializers.SerializerMethodField('get_display_type')
	uchi = UChiYoSoSerializer()
	yoso = UChiYoSoSerializer()

	class Meta:
		model = Word

	def get_display_type(self, obj):
		#顯示原本的字串obj.get_foo_display()
		return obj.get_type_display()

class GetWordVerbSerializer(serializers.ModelSerializer):
	display_type = serializers.SerializerMethodField('get_display_type')
	type = serializers.SerializerMethodField('get_type')
	uchi = UChiYoSoSerializer()
	yoso = UChiYoSoSerializer()

	class Meta:
		model = Word

	def get_display_type(self, obj):
		return u"動詞"

	def get_type(self, obj):
		return u"verb"


class SearchWordSerializer(serializers.Serializer):
	word = serializers.CharField(required=False)
	level = serializers.CharField()
	number = serializers.CharField()
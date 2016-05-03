#-*- encoding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from course.models import Word, Verb, UChiYoSo, Grammar, GrammarImage, GrammarExample

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
	#type = serializers.SerializerMethodField('get_type')
	uchi = UChiYoSoSerializer()
	yoso = UChiYoSoSerializer()

	class Meta:
		model = Verb

	def get_display_type(self, obj):
		return u"動詞"

class SearchWordSerializer(serializers.Serializer):
	word = serializers.CharField(required=False)
	level = serializers.CharField()
	number = serializers.CharField()

class SearchGrammarSerializer(serializers.Serializer):
	level = serializers.CharField()
	number = serializers.CharField()

class GrammarExampleSerializer(serializers.ModelSerializer):

	class Meta:
		model = GrammarExample

class GrammarImageSerializer(serializers.ModelSerializer):
	image = serializers.SerializerMethodField('get_image_url')

	class Meta:
		model = GrammarImage

	def get_image_url(self, obj):
		return urlparse.urljoin(Site.objects.get_current().domain, obj.image.url)

class GetGrammarSerializer(serializers.ModelSerializer):
	examplies = serializers.SerializerMethodField('get_examplies')
	images = serializers.SerializerMethodField('get_images')

	class Meta:
		model = Grammar

	def get_examplies(self, obj):
		examplies_serializer = GrammarExampleSerializer(obj.grammar_example.all(), many=True)
		return examplies_serializer.data

	def get_images(self, obj):
		images_serializer = GrammarImageSerializer(obj.grammar_image.all(), many=True)
		return images_serializer.data


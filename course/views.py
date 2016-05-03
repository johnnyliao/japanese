# -*- encoding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from course.models import Word, Verb, Grammar
from course.serializers import GetWordSerializer, SearchWordSerializer, GetStartLimitDataSerializer, GetWordVerbSerializer, SearchGrammarSerializer, GetGrammarSerializer
from django.contrib import auth
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils import simplejson
from django.db.models import Avg
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import math
import datetime
from django.utils import timezone
from django.db.models import Q, Count
from itertools import chain
from django.http.request import QueryDict, MultiValueDict


class GetWordView(generics.GenericAPIView):
	serializer_class = GetStartLimitDataSerializer
	permission_classes = (AllowAny, )

	def get(self, request):
		"""
		取得所有單字
		"""

		serializer = GetWordSerializer(Word.objects.all(), many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class SearchWordView(generics.GenericAPIView):
	serializer_class = SearchWordSerializer
	permission_classes = (AllowAny, )

	def post(self, request):
		"""
		搜尋單字
		"""

		serializer = self.serializer_class(data=request.DATA)
		if serializer.is_valid():
			word = serializer.data.get('word', None)
			level = serializer.data.get('level')
			number = serializer.data.get('number')

			word_objects_all = Word.objects.all()
			verb_objects_all = Verb.objects.all()

			if level != "all":
				word_objects_all = word_objects_all.filter(level=level)
				verb_objects_all = verb_objects_all.filter(level=level)

			if number != "all":
				word_objects_all = word_objects_all.filter(number=number)
				verb_objects_all = verb_objects_all.filter(number=number)

			if word:
				word_objects_all = word_objects_all.filter(Q(kanji=word) | Q(kana=word) | Q(chinese__contains=word))
				verb_objects_all = verb_objects_all.filter(Q(kanji=word) | Q(kana=word) | Q(chinese__contains=word))

			word_serializer = GetWordSerializer(word_objects_all, many=True)
			verb_serializer = GetWordVerbSerializer(verb_objects_all, many=True)

			result = word_serializer.data + verb_serializer.data


			return Response(result, status=status.HTTP_200_OK)

		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchGrammarView(generics.GenericAPIView):
	serializer_class = SearchGrammarSerializer
	permission_classes = (AllowAny, )

	def post(self, request):
		"""
		搜尋文法
		"""

		serializer = self.serializer_class(data=request.DATA)
		if serializer.is_valid():
			level = serializer.data.get('level')
			number = serializer.data.get('number')

			grammar_all = Grammar.objects.all()

			if level != "all":
				grammar_all = grammar_all.filter(level=level)

			if number != "all":
				grammar_all = grammar_all.filter(number=number)


			grammar_serializer = GetGrammarSerializer(grammar_all, many=True)

			return Response(grammar_serializer.data, status=status.HTTP_200_OK)

		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



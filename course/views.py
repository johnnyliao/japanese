# -*- encoding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from course.models import Word, Verb
from course.serializers import GetWordSerializer, SearchWordSerializer, GetStartLimitDataSerializer
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

			if word:
				search_words = Word.objects.all().filter(Q(kanji=word) | Q(kana=word) | Q(chinese=word))
				#無單字 搜尋動詞
				if not search_words:
					search_words = Verb.objects.all().filter(Q(kanji=word) | Q(kana=word) | Q(chinese=word))

				result_serializer = GetWordSerializer(search_words, many=True)

				return Response(result_serializer.data, status=status.HTTP_200_OK)
			else:
				return Response([], status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


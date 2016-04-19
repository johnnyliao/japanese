# -*- encoding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from course.models import Word, Verb
from course.serializers import GetWordSerializer, GetStartLimitDataSerializer
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

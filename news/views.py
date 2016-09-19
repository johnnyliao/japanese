# -*- encoding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from news.models import News, NewsAudio, NewsPhoto, AWS
from news.serializers import NewsSerializers
from django.contrib import auth
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils import simplejson
from django.db.models import Avg
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import math
import datetime
import requests
import os
import boto
import settings
from django.utils import timezone
from django.db.models import Q, Count
from itertools import chain
from django.http.request import QueryDict, MultiValueDict
from django.core.exceptions import ObjectDoesNotExist
from boto.s3.key import Key

class UpdateNewsView(generics.GenericAPIView):
	serializer_class = NewsSerializers
	permission_classes = (AllowAny, )

	def get(self, request):
		"""
		更新news
		"""
		r = requests.get('http://mazii.net/api/news/1/10')
		if r.status_code != 200:
			return Response("news connect fail", status=status.HTTP_200_OK)

		for item in r.json()['results']:
			news_id = item['id']

			try:
				news = News.objects.get(news_id=news_id)
				print "id exiets continue"
				continue
			except ObjectDoesNotExist:
				r = requests.get('http://mazii.net/api/news/' + news_id)

				if r.status_code != 200:
					return Response("news connect fail", status=status.HTTP_200_OK)

				result = r.json()['result']
				rev = result['_rev']
				title = result['title']
				link = result['link']
				pubdate = result['pubDate']
				description = result['description']
				content = result['content']['textbody']
				pubdate = datetime.datetime.strptime(pubdate, "%Y-%m-%d %H:%M:%S")
				news = News(news_id=news_id, rev=rev, title=title, link=link, pubdate=pubdate, description=description, content=content)
				news.save()

				pres_file_from_website(news, result['content']['audio'], "audio")

				#pres_file_from_website(news, result['content']['image'])
			break
		return Response("ok", status=status.HTTP_200_OK)


def pres_file_from_website(news, filename, type):
	print "downloading with requests"
	file_name = filename.split('.')
	url = 'http://www3.nhk.or.jp/news/easy/' + file_name[0] + '/' + filename
	print url
	r = requests.get(url)
	fn = "/tmp/"+filename
	with open(fn, "wb") as code:
		code.write(r.content)

	url = upload_file_to_s3(filename, fn)
	if url:
		news_audio = NewsAudio(news=news, path=url)
		news_audio.save()
	else:
		print "upload to s3 fail"
		pass

def upload_file_to_s3(filename, fn):
	# connect to the bucket
	aws = AWS.objects.all()[0]
	conn = boto.connect_s3(aws.key_id, aws.s_key)
	bucket = conn.get_bucket("johnny.liao")
	# go through each version of the file
	# create a key to keep track of our file in the storage
	k = Key(bucket)
	k.key = filename
	if k.set_contents_from_filename(fn):
		k.make_public()
		print "upload done....."
		url = k.generate_url(expires_in=0, query_auth=False, force_http=True)
		print url
		return url
	else:
		return False

#-*- encoding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from news.models import News

from rest_framework import serializers

from datetime import datetime,timedelta
from django.utils import timezone
import urlparse
from django.contrib.sites.models import Site
from news.models import News

class NewsSerializers(serializers.ModelSerializer):

	class Meta:
		model = News


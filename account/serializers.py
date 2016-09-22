#-*- encoding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from account.models import User
from allauth.socialaccount.models import (SocialLogin, SocialToken, SocialAccount)
from main.serializers import GetStartLimitDataSerializer
from game.serializers import ActionListInfoSerializer, GiftListInfoSerializer
from main.serializers import AdvertisementInfoSerializer
from rest_framework import serializers

from django.contrib.auth import get_user_model
import pytz
from datetime import datetime, timedelta

class FacebookConnectSerializer(serializers.Serializer):
    access_token = serializers.CharField()


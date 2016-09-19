
from django.conf.urls import patterns, url
from news.views import *

urlpatterns = patterns("news.views",
   	url('^update_news/', UpdateNewsView.as_view()),
)

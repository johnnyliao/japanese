
from django.conf.urls import patterns, url
from news.views import *

urlpatterns = patterns("news.views",
   	url('^update_news/', UpdateNewsView.as_view()),
   	url('^get_news/', GetNewsView.as_view()),
)

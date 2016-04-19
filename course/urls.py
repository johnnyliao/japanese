
from django.conf.urls import patterns, url
from course.views import *

urlpatterns = patterns("course.views",

   	url('^get_word/', GetWordView.as_view()),
)

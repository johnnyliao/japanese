
from django.conf.urls import patterns, url
from course.views import *

urlpatterns = patterns("course.views",

   	url('^get_word/', GetWordView.as_view()),
   	url('^search_word/', SearchWordView.as_view()),
   	url('^search_grammar/', SearchGrammarView.as_view()),
)

from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url

from pressman import views

urlpatterns = patterns('',
       url(r'^detail/(?P<pid>\d+)/$', 'pressman.views.detail'),
       url(r'^latest/$', 'pressman.views.latest'),
       url(r'^list/$', 'pressman.views.pressman_list'),
       url(r'^$', 'django.views.generic.simple.redirect_to',
           {'url':'/pressman/list/'}),
)
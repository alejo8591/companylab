from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       (r'^detail/(?<pid>\d+)/$', 'pressman.views.detail'),
)


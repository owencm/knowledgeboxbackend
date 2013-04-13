from django.conf.urls import patterns, url

from backend import views

urlpatterns = patterns('',
    url(r'^qaitems/$', views.qaitem_index, name='qaitem_index'),
    url(r'^qaitems/(?P<qaitem_id>\d+)$', views.qaitem, name='qaitem')
)
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from backend.views import QaItemList, QaItemDetail

from backend import views

urlpatterns = patterns('',
    url(r'^qaitems/$', QaItemList.as_view(), name='qaitem_list'),
    url(r'^qaitems/(?P<pk>\d+)$', QaItemDetail.as_view(), name='qaitem_details')
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
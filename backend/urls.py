from django.conf.urls import patterns, url
# from rest_framework.urlpatterns import format_suffix_patterns
# from backend.views import QaItemList, QaItemDetail

from backend import views

urlpatterns = patterns('',
	url(r'^qaitems/$', views.qaitem_index, name='qaitem-index'),
	url(r'^qaitems/id/(?P<qaitem_id>\d+)$', views.qaitem, name='qaitem-detail'),
	url(r'^qaitems/id/(?P<qaitem_id>\d+)/learn/$', views.qaitem_learn, name='qaitem-learn'),
	url(r'^qaitems/id/(?P<qaitem_id>\d+)/forget/$', views.qaitem_forget, name='qaitem-forget'),
	url(r'^qaitems/url/(?P<url>.+)$', views.qaitem_index_filter_by_url, name='qaitem-filter-by-url'),
	url(r'^qaitems/user/(?P<user_id>\d+)/$', views.qaitem_index_filter_by_learning, name='qaitem-filter-by-learning'),
	url(r'^qaitems/user/(?P<user_id>\d+)/url/(?P<url>.+)$', views.qaitem_index_filter_by_url_including_learning, name='qaitem-filter-by-url-including-learning'),
	url(r'^qresponse/$', views.qresponse, name='qresponse'),



	url(r'^login/$', views.login, name='login'),
	url(r'^register/$', views.register, name='register'),


	# url(r'^qaitems/$', QaItemList.as_view(), name='qaitem_list'),
	# url(r'^qaitems/(?P<pk>\d+)$', QaItemDetail.as_view(), name='qaitem_details')
)

# # Format suffixes
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
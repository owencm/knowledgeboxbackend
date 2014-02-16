from django.conf.urls import patterns, url

from backend import views

urlpatterns = patterns('',
	url(r'^qaitems/$', views.qaitem_index, name='qaitem-index'),
	url(r'^qaitems/id/(?P<qaitem_id>\d+)$', views.qaitem, name='qaitem-detail'),
	url(r'^qaitems/id/(?P<qaitem_id>\d+)/learn/$', views.qaitem_learn, name='qaitem-learn'),
	url(r'^qaitems/id/(?P<qaitem_id>\d+)/forget/$', views.qaitem_forget, name='qaitem-forget'),
	url(r'^qaitems/url/(?P<url>.+)$', views.qaitem_index_filter_by_url, name='qaitem-filter-by-url'),
	url(r'^qaitems/user/(?P<user_id>\d+)/$', views.qaitem_index_filter_by_learning, name='qaitem-filter-by-learning'),
	url(r'^qaitems/user/(?P<user_id>\d+)/url/(?P<url>.+)$', views.qaitem_index_filter_by_url_including_learning, name='qaitem-filter-by-url-including-learning'),
	# Not sure how to use these
	# url(r'^login/$', views.login, name='login'),
	# url(r'^register/$', views.register, name='register'),
)

# # Format suffixes
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
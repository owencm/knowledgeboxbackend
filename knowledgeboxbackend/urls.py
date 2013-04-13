from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'knowledgeboxbackend.views.home', name='home'),
    # url(r'^knowledgeboxbackend/', include('knowledgeboxbackend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'', include('backend.urls')),

    # Uncomment the next line to enable the admin:
    # social-auth
	url(r'', include('social_auth.urls')),

	# rest-framework
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    # site admin
    url(r'^admin/', include(admin.site.urls)),
)

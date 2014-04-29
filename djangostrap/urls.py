from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'djangostrap.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    (r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve'),
    (r'^media/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve'),
)

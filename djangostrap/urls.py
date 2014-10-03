from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap
from django.contrib import admin
from djangostrap import settings

admin.autodiscover()

class ViewSitemap(Sitemap):
  """Reverse static views for XML sitemap."""
  def items(self):
    return [
      'index',
      # add your views here
    ]

  def location(self, item):
    try:
      return reverse(item)
    except Exception, e:
      return reverse("index")

sitemaps = {'views': ViewSitemap}


urlpatterns = patterns('',

    url(r'^$', 'djangostrap.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),

    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)

if settings.DEBUG is True:
  urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve'),
    url(r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve'),
  )


handler400 = 'djangostrap.views.handler400'
handler403 = 'djangostrap.views.handler403'
handler404 = 'djangostrap.views.handler404'
handler500 = 'djangostrap.views.handler500'
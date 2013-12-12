from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from rcbweb.views import index

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rcbweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rcb/([A-Za-z0-9]*)[/]?$', index),
)

urlpatterns += staticfiles_urlpatterns()

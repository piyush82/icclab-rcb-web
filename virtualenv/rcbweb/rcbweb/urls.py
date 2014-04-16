from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from rcbweb.views import index
from rcbweb.views import login
from rcbweb.views import worker
from rcbweb.views import doaction

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rcbweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rcb/$', index),
    url(r'^rcb/demo/$', login),
    url(r'^rcb/demo/([A-Za-z0-9]*)[/]?$', worker),
    url(r'^rcb/demo/action/([A-Za-z0-9]*)[/]?$', doaction),
)

urlpatterns += staticfiles_urlpatterns()

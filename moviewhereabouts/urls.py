from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moviewhereabouts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^asteroid/', include('asteroid.urls', namespace="asteroid")),
    url(r'^admin/', include(admin.site.urls)),
)

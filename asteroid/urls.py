from django.conf.urls import patterns, url

from asteroid import views

urlpatterns = patterns('',
    url(r'^$', views.screen1, name='screen1'),
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^browse/$', views.browse, name='browse'),
    url(r'^browse-genre/(?P<g>\w+)/$', views.browse_genre, name='browse_genre'),
    url(r'^search/$', views.search, name='search'),
    url(r'^index/$', views.index, name='index'),
    url(r'^indextop/$', views.indextop, name='indextop'),
    url(r'^(?P<movie_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<movie_id>\d+)/voting/$', views.voting, name='voting'),
)



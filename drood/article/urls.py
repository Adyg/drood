from django.conf.urls import patterns, url

urlpatterns = patterns('article.views',
                       url(r'^$', 'list', name='home'),
                       url(r'^feed/(?P<feed_id>\d+)/$', 'list', name='home-feed'),)

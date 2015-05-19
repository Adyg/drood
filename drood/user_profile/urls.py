from django.conf.urls import patterns, url

urlpatterns = patterns('user_profile.views',
                       url(r'^upload/opml/$', 'upload_opml', name='upload_opml'),
                       )

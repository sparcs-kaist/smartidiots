from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'apps.member.views.list'),
    url(r'^(?P<username>\w+)$', 'apps.member.views.detail'),
)

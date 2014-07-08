from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'apps.seminar.views.list'),
)

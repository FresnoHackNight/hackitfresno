from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.Homepage.as_view(), name='index'),
    url(r'^rules/$', views.Rules.as_view(), name='rules'),
    url(r'^prizes/$', views.Prizes.as_view(), name='prizes'),
    url(r'^coc/$', views.CodeOfConduct.as_view(), name='coc'),

    url(r'^404/$', views.Error404.as_view(), name='404'),
    url(r'^500/$', views.Error500.as_view(), name='500'),
)

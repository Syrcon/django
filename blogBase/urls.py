#coding: utf-8

from django.conf.urls import patterns, url
from blogBase.views import PostsListView

urlpatterns = patterns('',
	url(r'^$', PostsListView.as_view(), name='list'),
	url(r'^(?P<pk>\d+)/$', 'blogBase.views.view_post', name='blog_post_detail'),
    url(r'^add_post/$', 'blogBase.views.add_post', name='blog_post_add'),
)

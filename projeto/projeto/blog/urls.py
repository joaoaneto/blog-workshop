#-*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
import views

urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^post/(?P<pk>\d+)/$', views.post_details),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit),
	url(r'^post/new/$', views.post_new),
]
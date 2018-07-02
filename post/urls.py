#coding=utf-8

from django.conf.urls import url
import views


urlpatterns = [
    url('^$',views.showAll),
    url('^page/(\d+)$',views.showAll),
    url('^post/(\d+)$',views.detail),
    url('^category/(\d+)$',views.getPostsByCid),
    url('^archive/(\d{4})/(\d{2})$',views.getPostsByCreated),
]
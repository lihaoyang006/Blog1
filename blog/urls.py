#-*- encoding: utf-8 -*-

from django.conf.urls import url
from blog.views import index

urlpatterns = [
    url(r'^index/', index),
]
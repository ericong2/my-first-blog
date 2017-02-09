# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 15:36:07 2017

@author: eric ong
"""

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
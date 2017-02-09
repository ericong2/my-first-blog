# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 10:24:20 2017

@author: eric ong
"""

from django.conf.urls import url

from . import views

urlpatterns = [url(r'^$', views.index, name='index'),
]
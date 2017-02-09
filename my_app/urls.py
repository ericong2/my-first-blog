# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 10:33:44 2017

@author: eric ong
"""

from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.hello, name='hello'),]
                       
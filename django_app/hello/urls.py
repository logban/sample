#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 00:40:24 2019

@author: logban
"""
from django.urls import path
from . import views
urlpatterns = [
        path('', views.index, name='index'),
        path('create', views.create, name = 'create'),
        path('hanei', views.hanei, name='hanei'),
]
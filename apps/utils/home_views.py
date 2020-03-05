# -*- coding: utf-8 -*-
# @Time    : 3/4/20 11:20 PM
# @Author  : naturegong
# @File    : home_views.py
from django.shortcuts import render


def home_view(request):
    """
    替换首页
    """
    return render(request, 'index.html')
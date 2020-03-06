# -*- coding: utf-8 -*-
# @Time    : 3/5/20 3:54 PM
# @Author  : naturegong
# @File    : sentry_test.py

from django.urls import path


def trigger_error(request):
    division_by_zero = 1 / 0

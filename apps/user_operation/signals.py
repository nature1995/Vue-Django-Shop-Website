# -*- coding: utf-8 -*-
# @Time    : 2/27/20 5:52 PM
# @Author  : naturegong
# @File    : signals.py
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model

from user_operation.models import UserFav


# 参数一接收哪种信号，参数二是接收哪个model的信号
@receiver(post_save, sender=UserFav)
def create_user_fav(sender, instance=None, created=False, **kwargs):
    # 是否新建，因为update的时候也会进行post_save
    if created:
        goods = instance.goods
        goods.fav_num += 1
        goods.save()


# 参数一接收哪种信号，参数二是接收哪个model的信号
@receiver(post_delete, sender=UserFav)
def del_user_fav(sender, instance=None, created=False, **kwargs):
    goods = instance.goods
    goods.fav_num -= 1
    goods.save()

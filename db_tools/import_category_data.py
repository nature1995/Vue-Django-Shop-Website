# -*- coding: utf-8 -*-
# @Time    : 2/15/20 3:50 PM
# @Author  : naturegong
# @File    : import_category_data.py

# 独立使用django的model
import sys
import os

#  获取当前文件的路径，以及路径的父级文件夹名
pwd = os.path.dirname(os.path.realpath(__file__))
# 将项目目录加入setting
sys.path.append(pwd + "../")
# manage.py中
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VueDjangoShopWebsite.settings')

import django

django.setup()

# 这行代码必须在初始化django之后
from goods.models import GoodsCategory

all_category = GoodsCategory.objects.all()

from db_tools.data.category_data import row_data

# 一级分类
for lev1_cat in row_data:
    lev1_instance = GoodsCategory()
    lev1_instance.code = lev1_cat["code"]
    lev1_instance.name = lev1_cat["name"]
    lev1_instance.category_type = 1
    lev1_instance.save()

    # 该一级分类之下的二级分类
    for lev2_cat in lev1_cat["sub_categorys"]:
        lev2_instance = GoodsCategory()
        lev2_instance.code = lev2_cat["code"]
        lev2_instance.name = lev2_cat["name"]
        lev2_instance.category_type = 2
        lev2_instance.parent_category = lev1_instance
        lev2_instance.save()

        # 该二级分类之下的三级分类
        for lev3_cat in lev2_cat["sub_categorys"]:
            lev3_instance = GoodsCategory()
            lev3_instance.code = lev3_cat["code"]
            lev3_instance.name = lev3_cat["name"]
            lev3_instance.category_type = 3
            lev3_instance.parent_category = lev2_instance
            lev3_instance.save()

# -*- coding: utf-8 -*-
# @Time    : 2/16/20 4:44 PM
# @Author  : naturegong
# @File    : views_base.py

from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
import json

from goods.models import Goods


class GoodsListView(View):
    def get(self, request):
        """
        通过django的view实现商品列表页
        :param request:
        :return:
        """
        json_list = []
        goods = Goods.objects.all()[:10]

        # for good in goods:
        #     json_dict = {"name": good.name, "category": good.category.name, "market_price": good.market_price}
        #     json_list.append(json_dict)

        for good in goods:
            json_dict = model_to_dict(good)
            json_list.append(json_dict)

        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)

        # jsonResponse做的工作也就是加上了dumps和content_type
        # return HttpResponse(json.dumps(json_data), content_type="application/json")
        # 注释掉loads，下面语句正常
        # return HttpResponse(json_data, content_type="application/json")
        return JsonResponse(json_data)

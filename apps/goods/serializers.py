# -*- coding: utf-8 -*-
# @Time    : 2/16/20 6:12 PM
# @Author  : naturegong
# @File    : serializers.py
from rest_framework import serializers
from goods.models import Goods, GoodsCategory, GoodsImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'


# class GoodsImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GoodsImage
#         fields = ("image",)


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        # fields = ('category', 'goods_sn', 'name', 'click_num', 'sold_num', 'market_price')
        fields = '__all__'


# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Goods` instance, given the validated data.
#         """
#         return Goods.objects.create(**validated_data)







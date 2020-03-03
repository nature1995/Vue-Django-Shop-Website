# -*- coding: utf-8 -*-
# @Time    : 3/2/20 4:17 PM
# @Author  : naturegong
# @File    : serializers.py
import re
from rest_framework import serializers
from user_operation.models import UserFav, UserLeavingMessage, UserAddress
from goods.serializers import GoodsSerializer
from rest_framework.validators import UniqueTogetherValidator
from VueDjangoShopWebsite.settings import REGEX_MOBILE


class UserFavDetailSerializer(serializers.ModelSerializer):
    # 通过goods_id拿到商品信息。就需要嵌套的Serializer
    goods = GoodsSerializer()

    class Meta:
        model = UserFav
        fields = ("goods", "id")


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="已经收藏"
            )
        ]
        fields = ("user", "goods", "id")


class LeavingMessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserLeavingMessage
        fields = ("id", "user", "message_type", "subject", "message", "file", "add_time")


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    def validate_signer_mobile(self, signer_mobile):
        """
        验证电话是否合法
        """
        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, signer_mobile):
            raise serializers.ValidationError("手机号码非法")
        return signer_mobile

    class Meta:
        model = UserAddress
        fields = ("id", "user", "province", "city", "district", "address", "signer_name", "signer_mobile", "add_time")

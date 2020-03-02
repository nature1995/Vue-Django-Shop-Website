import random

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import status
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from VueDjangoShopWebsite.settings import APIKEY
from users.models import VerifyCode
from users.serializers import SmsSerializer, UserRegSerializer
from utils.yunpian import YunPian
from utils.tencent_sms import TencentSms
from VueDjangoShopWebsite.settings import (
    TENCENT_SECRET_ID, TENCENT_SECRET_KEY
)

User = get_user_model()
# Create your views here.


class CustomBackend(ModelBackend):
    """
    自定义用户验证规则
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因
            # 后期可以添加邮箱验证
            user = User.objects.get(
                Q(username=username) | Q(mobile=username))
            # django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有def check_password(self,
            # raw_password):
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class SmsCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    发送短信验证码
    """
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成四位数字的验证码字符串
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(random.choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        """
        使用云片发送短信
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = self.get_serializer(data=request.data)
        # 验证合法
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data["mobile"]

        # 使用云片发送短信
        yun_pian = YunPian(APIKEY)

        # 生成验证码
        code = self.generate_code()

        # 使用云片发送短信
        sms_status = yun_pian.send_sms(code=code, mobile=mobile)

        if sms_status["code"] != 0:
            return Response({
                "mobile": sms_status["msg"]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                "mobile": mobile
            }, status=status.HTTP_201_CREATED)

    # def create(self, request, *args, **kwargs):
    #     """
    #     使用腾讯云短信平台发送短信
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     serializer = self.get_serializer(data=request.data)
    #     # 验证合法
    #     serializer.is_valid(raise_exception=True)
    #     mobile = serializer.validated_data["mobile"]
    #
    #     # 使用腾讯云短信平台发送短信
    #     tencent_sms = TencentSms(TENCENT_SECRET_ID, TENCENT_SECRET_KEY)
    #
    #     # 生成验证码
    #     code = self.generate_code()
    #
    #     sms_status = tencent_sms.send_sms(code=code, mobile="+86".join(mobile))
    #
    #     if sms_status["SendStatusSet"][0]["Code"] != 0:
    #         return Response({
    #             "mobile": sms_status["SendStatusSet"][0]["Message"]
    #         }, status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         code_record = VerifyCode(code=code, mobile=mobile)
    #         code_record.save()
    #         return Response({
    #             "mobile": mobile
    #         }, status=status.HTTP_201_CREATED)


class UserViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data

        # 生成注册用户的Token
        re_dict["token"] = str(AccessToken.for_user(user))
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)

        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

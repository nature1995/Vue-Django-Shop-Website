from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from utils.permissions import IsOwnerOrReadOnly
from .models import UserFav
from .serializers import UserFavSerializer
# Create your views here.


class UserFavViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    """
    用户收藏
    """
    # queryset = UserFav.objects.all()
    # permission是用来做权限判断的
    # IsAuthenticated：必须登录用户；IsOwnerOrReadOnly：必须是当前登录的用户
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # auth使用来做用户认证的
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    serializer_class = UserFavSerializer
    # 搜索的字段
    lookup_field = 'goods_id'

    # 重载查询方法，只查询当前用户的收藏列表
    def get_queryset(self):
        # 只能查看当前登录用户的收藏，不会获取所有用户的收藏
        return UserFav.objects.filter(user=self.request.user)

"""VueDjangoShopWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from django.views.static import serve

from VueDjangoShopWebsite.settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from goods.views import GoodsListViewSet, CategoryViewset
from users.views import SmsCodeViewset, UserViewset
from user_operation.views import UserFavViewset, LeavingMessageViewset
import xadmin

# goods_list = GoodsListViewSet.as_view({
#     'get': 'list',
# })
router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet, basename="goods")
# 配置category的url
router.register(r'categorys', CategoryViewset, basename="categorys")
# 配置codes的url
router.register(r'code', SmsCodeViewset, basename="code")
# 配置users的url
router.register(r'users', UserViewset, basename="users")
# 配置用户收藏的url
router.register(r'userfavs', UserFavViewset, basename="userfavs")
# 配置用户留言的url
router.register(r'messages', LeavingMessageViewset, basename="messages")


urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    # 调试登录
    url(r'^api-auth/', include('rest_framework.urls')),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，传入配置好的MEDIAROOT
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    # 商品列表页
    # url(r'goods/$', goods_list, name="goods-list"),
    path('', include(router.urls)),
    # 自动生成文档
    url(r'docs/', include_docs_urls(title="生鲜超市文档")),
    # drf自带的token授权登录,获取token需要向该地址post数据
    url(r'^api-token-auth/', views.obtain_auth_token),

    url(r'^login/', TokenObtainPairView.as_view(), name='login'),
    url(r'^api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

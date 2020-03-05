from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.authentication import (
    SessionAuthentication, BasicAuthentication, TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from .models import (
    Goods, GoodsCategory, Banner, HotSearchWords
)
from .filters import GoodsFilter
from .serializers import (
    GoodsSerializer, CategorySerializer, BannerSerializer,
    IndexCategorySerializer, HotWordsSerializer
)


class GoodsPagination(PageNumberPagination):
    # 默认每页显示的个数
    page_size = 12
    # 动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = "page"
    # 最多能显示多少页
    max_page_size = 100


# class GoodsListView(APIView):
#     """
#     商品列表页
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)
#
#     def post(self, request, format=None):
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoodsListView(generics.ListAPIView):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination


class GoodsListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    商品列表页，分页，搜索，过滤，排序
    """
    # 这里必须要定义一个默认的排序,否则会报错
    queryset = Goods.objects.all().order_by('id')
    # 序列化
    serializer_class = GoodsSerializer
    # 分页
    pagination_class = GoodsPagination
    # 缓存
    throttle_classes = (UserRateThrottle, AnonRateThrottle)

    # authentication_classes = (BasicAuthentication, SessionAuthentication, JWTAuthentication, )
    # permission_classes = [IsAuthenticated]
    # 设置三大常用过滤器之DjangoFilterBackend, SearchFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # 设置filter的类为我们自定义的类
    filter_class = GoodsFilter
    # filterset_fields = ['name', 'shop_price']
    # 设置我们的search字段
    search_fields = ('name', 'goods_brief', 'goods_desc')
    # 设置排序
    ordering_fields = ('sold_num', 'shop_price')

    # 商品点击数+1
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get("price_min", 0)
    #     if price_min:
    #         queryset = Goods.objects.filter(shop_price__gt=int(price_min))
    #     return queryset


class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取轮播图列表
    """
    queryset = Banner.objects.all().order_by("index")
    serializer_class = BannerSerializer


class IndexCategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    首页商品分类数据
    """
    # 获取is_tab=True（导航栏）里面的分类下的商品数据
    queryset = GoodsCategory.objects.filter(is_tab=True, name__in=["生鲜食品", "酒水饮料"])
    serializer_class = IndexCategorySerializer


class HotSearchsViewset(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    获取热搜词列表
    """
    queryset = HotSearchWords.objects.all().order_by("-index")
    serializer_class = HotWordsSerializer

[Django REST framework+Vue 前后端分离生鲜超市](https://github.com/nature1995/Vue-Django-Shop-Website.git)
-------------------------------------------------------------------
[![python3](https://img.shields.io/badge/python-3-blue.svg)]()
[![django3.0.0](https://img.shields.io/badge/django-3.0.0-brightgreen.svg)]()


#### 前端：
- Vue 

#### 后端：
- Python 3.6, 3.7 and 3.8
- Django 1.11, 2.1, 2.2 and 3.0
- Django Rest Framework 3.9, 3.10 and 3.11

-----------------------

## 一、项目介绍
### 1.1.掌握的技术

1.  Vue + Django Rest Framework 前后端分离技术 
2.  彻底玩转restful api 开发流程
3.  Django Rest Framework 的功能实现和核心源码分析
4.  Sentry 完成线上系统的错误日志的监控和告警   
5.  第三方登录和支付宝支付的集成  
6.  本地调试远程服务器代码的技巧
    

### 1.2.系统构成

1.  vue前端项目  
2.  django rest framework 系统实现前台功能   
3.  xadmin后台管理系统
    

vue部分:

*   API 接口   
*   Vue 组件 与api的交互    
*   vue的项目组织结构分析   

Django Rest Framework 技能

*   通用view实现 rest api接口
*   apiview方式实现api   
*   genericView方式实现api接口   
*   Viewset和router方式实现api接口和url配置   
*   Django\_filter searchFilter OrderFilter 分页    
*   通用mixin    
*   权限和认证；
*   Authentication用户认证设置   
*   动态设置permission、authentication    
*   Validators实现字段验证
*   序列化和表单验证
*   Serializer   
*   ModelSerializer   
*   动态设置Serializer
*   支付登录注册
*   json web token 实现登录    
*   手机注册    
*   支付宝支付  
*   第三方登录
*   进阶开发
*   Django rest framework 部分核心源码解读    
*   文档自动化管理   
*   django rest framework的缓存  
*   throttling 对用户和ip进行限速
    
### 1.3.开发中常见的问题

*   本地系统不能重现的bug    
*   api接口出错不能及时的发现或难以找到错误栈    
*   api文档管理问题，html markdown    
*   大量的url配置造成url配置越来越多难以维护    
*   接口不及时去更新文档，对方不知道如何去测试接口，但写文档会花费大量的时间去维护.
    
*   为了防止爬虫，我们需要针对api的访问频率进行限制，比如一分钟，一小时，或者一天用户的访问频率限制问题。   
*   某些页面将数据放入缓存，加速某些api的访问速度
    

### 1.4.开发中常见问题解决方案

1.  通过介绍pycharm 的远程服务器代码调试技巧让大家不仅可以调试支付，第三方登录，还可以远程服务器代码来重现服务器上的bug    
2.  通过docker 搭建 sentry 来体验错误日志监控系统，让我们不仅可以得到线上的错误栈还能及时在发生系统错误时收到邮件通知。   
3.  通过drf的文档自动化管理以及url的注册管理功能会让我们省去写文档的时间   
4.  django rest framework 的文档管理功能不仅可以让我们省去写文档的时间，还能直接在文档里面测试接口，自动生成js接口代码，shell测试代码和python测试代码   
5.  django rest framework 提供的throttle 对于api进行访问频率的限制 
6.  引入第三方框架来设置某些api的缓存
    
### 1.5.django进阶知识点

*   django mirgrations原理    
*   django 信号量    
*   django从请求到响应的完整过程    
*   独立使用django的model
    
### 1.6.vue知识点

*   vue技术选型分析
*   API后端数据填充到Vue组件模板 
*   Vue代码结构分析    

### 1.7.章节安排

*   项目介绍以及开发环境的搭建    
*   设计数据库以及导入原始数据   
*   restful api基础以及vue项目结构介绍    
*   商品列表页功能   
*   商品类别功能   
*   手机注册和用户登录  
*   商品详情页和收藏功能    
*   个人中心功能    
*   购物车、订单和支付宝支付功能    
*   首页，商品相关数量，缓存，访问限速功能    
*   第三方登录(微博 qq 微信)    
*   sentry系统错误日志监控

### 1.8.技术储备要求

*   django基础知识    
*   熟练掌握python语法    
*   了解vue & mysql基础
 
### 1.9.系统功能

*   分类 - 子分类 搜索 热搜词 购物车简要展示   
*   新品 分类展示， 大类的推荐商品。    
*   账户密码登录(json web token)。微博登录，输入账户跳转回首页。    
*   注册，手机号码注册，错误提示。倒计时功能，服务器端手机号码发送频次限制。   
*   商品大类，导航栏。筛选，排序。富文本。    
*   商品 收藏 加入购物车 结算，移出购物车    
*   留言 支付宝支付，扫码支付。跳回商户页面。    
*   订单详情，收货地址
*   个人信息，收藏商品，我的收藏。 
*   留言，上传文件。提交，删除留言
*   快速浏览。页面的缓存
*   访问速度限制 & 接口文档 测试交互 
*   出错处理: sentry基于drf。打印错误栈，当前请求用户。邮件通知
    
## 二、环境搭建

### 2.1.虚拟环境搭建

（1）环境变量设置
    # Mac
    无需配置，自动保存的./.virtualenvs/中
    #
*   桌面新建文件夹Envs  
*   新建环境变量：以后创建虚拟环境会自动保存到这个路径


（2）安装
```
pip install virtualenv

# Mac
pip install virtualenvwrapper # 并添加相应的环境变量到./.bash_profile中
workon #查看有哪些虚拟环境
workon VueDjango #进入创建的虚拟环境
deactivate #退出虚拟环境
activate #激活虚拟环境

# Win
pip install virtualenvwrapper\-win
mkvirtualenv VueDjango #创建虚拟环境
workon #查看有哪些虚拟环境
workon VueDjango #进入创建的虚拟环境
deactivate.bat #退出虚拟环境
activate.bat #激活虚拟环境
```

### 2.2.Vue环境搭建

（1）node.js

https://nodejs.org/

（2）cnpm

npm install -g cnpm --registry=https://registry.npm.taobao.org

（3）安装依赖

cnpm install

（4）运行

cnpm run dev

## 参考文档
Django3.0: https://docs.djangoproject.com/zh-hans/3.0/  
Django REST framework: https://www.django-rest-framework.org/     
DRF-extensions: http://chibisov.github.io/drf-extensions/docs/
xadmin: https://xadmin.readthedocs.io/en/docs-chinese/  
支付宝沙箱：https://openhome.alipay.com/platform/appDaily.htm  
腾讯云发送短信API: https://cloud.tencent.com/document/api/382/38778  



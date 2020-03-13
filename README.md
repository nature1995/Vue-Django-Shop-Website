# Django REST framework+Vue （生鲜超市后端代码）

-------------------------------------------------------------------

[![python3](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/downloads/)
[![django3.0.0](https://img.shields.io/badge/django-3.0.0-brightgreen.svg)](https://www.djangoproject.com/)


#### 前端：
- Vue 

#### 后端：
- Python 3.6, 3.7 and 3.8
- Django 1.11, 2.1, 2.2 and 3.0
- Django Rest Framework 3.9, 3.10 and 3.11

#### 提升与改进
1. 使用最新的django-rest-framework-simplejwt代替django-rest-framework-jwt，由于原作者已不再维护该项目。
2. 加入腾讯云短信发送相关代码
3. 配合django-rest-framework-simplejwt修复第三方登录时，用户前端显示bug。
4. 修复alipay密钥存储格式导致的Incorrect padding问题
5. 修复热门搜索接口
6. 可以切换数据库
7. 修复部分前端问题。

#### 项目资源
[Vue前端代码](https://github.com/nature1995/Vue-Django-Shop-Frontend)  
[Django后端代码](https://github.com/nature1995/Vue-Django-Shop-Website)

项目视频与原版文件: 链接:https://pan.baidu.com/s/1elQ0DJ-b0hB6W4ihJcK3mQ  密码:ndzt

-----------------------
## 项目内容

### 权限和认证
- Authentication用户认证设置
- 动态设置Permission、Authentication
- Validators实现字段验证

### 序列化和表单验证
- Serializer
- ModelSerializer
- 动态设置Serializer

### 支付、登录、注册
- Json Web Token方式登录
- 手机注册 / 支付宝支付
- 第三方登录

### View实现REST API

- Apiview方式实现API接口 / GenericView方式实现API接口
- Viewset和Router方式实现API接口和URL配置
- Django_filter、SearchFilter、OrderFilter、分页 / 通用Mixins

### 进阶开发
- Django REST framework部分核心源码解读
- 文档自动化管理 / Django REST framework的缓存
- Throttling对用户和IP进行限速

### Vue
Vue技术选型分析
API后端接口数据填充到Vue组件模板
Vue代码结构分析

### Django
- Django Mirgrations原理
- Django信号量
- Django从请求到响应的完整过程
- 独立使用Django的Model

### 实战内容
1. Vue+ Django REST framework前后端分离的全栈开发
2. Django REST framework的功能实现与核心源码分析
3. Sentry完成线上系统的错误日志的监控和告警
4. 第三方登录和第三方支付宝的支付集成
5. 本地调试远程服务器代码技巧

## 环境搭建

### 虚拟环境搭建

1. 环境变量设置
    **Mac**
    无需配置，自动保存的./.virtualenvs/中
    **Win**
    桌面新建文件夹Envs  
    新建环境变量：以后创建虚拟环境会自动保存到这个路径


2. 安装
```bash
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

3. 数据库选择
请选择其中一种数据库，新手推荐使用SQLite先运行，后面再数据同步与切换
```python
# 数据库选择SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 数据库选择MYSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vuedjango',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        "OPTIONS": {"init_command": "SET default_storage_engine=INNODB;"}
    }
}
```

### Vue环境搭建
**国内:**
1. node.js
https://nodejs.org/

2. cnpm
```bash
npm install -g cnpm --registry=https://registry.npm.taobao.org
```

4. 更改./src/api/api.js里的接口地址
```js
let local_host = 'http://127.0.0.1:8000';
```

5. 运行
```bash
cnpm run dev
```

**国外:**
1. node.js
https://nodejs.org/

2. 安装依赖
```
npm install
```

3. 运行
```
npm run dev
```
## 数据库部署
安装MySQL后在数据库中创建名为vueshop库，用下面代码导入SQL即可。
```bash
cd Vue-Django-Shop-Website/db_tools/
python import_category_data.py
python import_goods_data.py
```

## 配置与可选配置
```python
# 腾讯云短信设置
TENCENT_SECRET_ID = ''
TENCENT_SECRET_KEY = ''

# 云片网设置
APIKEY = ''

# 配置redis缓存
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "password"
        }
    }
}

SOCIAL_AUTH_WEIBO_KEY = ''
SOCIAL_AUTH_WEIBO_SECRET = ''
SOCIAL_AUTH_QQ_KEY = ''
SOCIAL_AUTH_QQ_SECRET = ''
SOCIAL_AUTH_WEIXIN_KEY = ''
SOCIAL_AUTH_WEIXIN_SECRET = ''

# 引入本地配置
try:
    from .local_settings import *
except ModuleNotFoundError as e:
    pass

# sentry初始化
sentry_sdk.init(
    dsn="You DNS address",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
```

## 参考文档
Django3.0: https://docs.djangoproject.com/zh-hans/3.0/  
Django REST framework: https://www.django-rest-framework.org/     
DRF-extensions: http://chibisov.github.io/drf-extensions/docs/  
django-rest-framework-simplejwt: https://github.com/davesque/django-rest-framework-simplejwt    
django-social-auth: https://github.com/omab/django-social-auth  
xadmin: https://xadmin.readthedocs.io/en/docs-chinese/  
支付宝沙箱：https://openhome.alipay.com/platform/appDaily.htm  
腾讯云发送短信API: https://cloud.tencent.com/document/api/382/38778  
django-redis 中文文档: https://django-redis-chs.readthedocs.io/zh_CN/latest/#  
Python Social Auth: https://python-social-auth.readthedocs.io/en/latest/  
redis数据库安装参考: https://www.jianshu.com/p/035be70daf2d


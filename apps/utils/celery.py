# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     celery
   Description :
   Author :       jusk?
   date：          2020/1/6
-------------------------------------------------
   Change Activity:
                   2020/1/6:
-------------------------------------------------
"""


from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings
# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_celery_demo.settings')
# 实例化Celery
app = Celery('task')
# 使用django的settings文件配置celery
app.config_from_object('django.conf.settings')
# Celery加载所有注册的应用
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     tasks
   Description :
   Author :       jusk?
   date：          2020/1/6
-------------------------------------------------
   Change Activity:
                   2020/1/6:
-------------------------------------------------
"""

import time

from utils.celery import app

#调度任务
@app.task
def add(x, y):
    # 模拟长时间耗时操作
    print('============耗时操作=============')
    time.sleep(10)
    print('============耗时操作结束============')
    return x + y
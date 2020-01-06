# django_app


[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)



>线上演示地址: http://45.77.189.214/admin/

>线上导入数据和创建默认账号地址:http://45.77.189.214/startdemo/
```markdown
自己演示的话直接将ip换成自己ip

一些api接口：http://45.77.189.214/api/

导入数据和创建账号接口：http://45.77.189.214/startdemo/

导入数据由于sqlite3不能的问题，可能一次只会导入几百条,多试几次就能直接全部导入完成


默认点了创建账号的接口
用户名:admin123456
密码:admin123456
```


## Quick Start

```
$ git clone https://github.com/jusk9527/django_app.git
$ cd django_app
$ docker-compose up
```
1. 注意已经安装了docker、docker-compose。未安装的[可参考这个](https://www.runoob.com/docker/centos-docker-install.html)
2. 注意自己配置setting中数据库，这是MYSQL的。生成环境还是MYSQL稳得
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',        #数据库名字
        'USER': '',          #账号
        'PASSWORD': '',    #密码

        'HOST': '',     #IP
        'PORT': '3306',          #端口
        #这里引擎用innodb（默认myisam）
        #因为后面第三方登录时，要求引擎为INNODB
        # 'OPTIONS':{'init_command': 'SET storage_engine=INNODB'},    #改为
        "OPTIONS":{"init_command":"SET default_storage_engine=INNODB;"}
    }
}
```
3. 由于是演示,故默认用的是sqlite3数据库。所有只是演示的如上Quick Start


4. celery 的一些使用技巧

#####  [django+celery 入门安装](https://github.com/coco369/knowledge/blob/master/celery/1.celery%E5%85%A5%E9%97%A8%E5%9F%BA%E7%A1%80/1.%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE%E4%B8%8E%E7%AE%80%E5%8D%95%E6%A1%88%E4%BE%8B.md)

#####  [django配置celery](https://juejin.im/post/5b588b8c6fb9a04f834655a6)

#####  [配置Django中Celery的定时任务与crontab讲解](https://www.jianshu.com/p/2e2a29e14c94)


```markdown
这个是可以做每天或定时时间做定时,配置参数做了比较详细的解释
```


#####  [django进阶之celery](https://segmentfault.com/a/1190000016082551)


```
经典命令
python manage.py celerybeat -l info
启动beat
```

##### [灵活多变的celery](https://github.com/celery)


```
这里有许多celery插件，比如:
django-celery-beat、这个是定时插件，比较灵活

django-celery-results、这个是执行结果存储,方便看执行结果是成功或者失败

还有许多
```

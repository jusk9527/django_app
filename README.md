# django_app


[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)



>线上演示地址: http://45.77.189.214/admin/
 
```markdown
一些api接口：http://45.77.189.214/api/

用户名:admin
密码:admin123
```


## Quick Start

```
$ git clone https://github.com/jusk9527/django_app.git
$ cd django_app
$ docker-compose up
```
1. 注意已经安装了docker、docker-compose
2. 注意自己配置setting中数据库

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

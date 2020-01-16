---
typora-root-url: img
---

## Django学习



启动 python manage.py runserver



Admin站点管理

配置Admin应用 在文件setings.py 配置 INSTALLED_APPS 内添加'django.contrib.admin'，默认是配置的。

创建管理员用户： 命令 python manage.py createsuperuser,

![1572872084237](/1572872084237.png)

setings.py 汉化修改

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

连接数据库： settings.py  内配置DATABASES

自带支持的数据库 mysql、 oracle、 postgresql、

![1572879726685](/1572879726685.png)

```
DATABASES = {

​    'default': {

​        'ENGINE': 'django.db.backends.postgresql_psycopg2',

​        'NAME': 'wyzx',

​        'USER': 'ots',

​        'PASSWORD': 'ots2017',

​        'HOST': 'localhost',

​        'PORT': '5432',

​        'CONN_MAX_AGE': 0 if DEBUG else 300,

​    }

}
```

管理数据表：   修改admin.py文件

from .models import Oils,Team

admin.site.register(Team)

admin.site.register(Oils)



管理页面自定义：

列表属性

​    list_display = ['name', 'shiftTime']  显示字段

​    list_filter = ['name'] 过滤字段

​    search_fields = ['name'] 搜索字段

​    list_per_page = 1 分页

```
class OilsAdmin(admin.ModelAdmin):

​    \#列表属性

​    list_display = ['name', 'code', 'densityScope', 'color', 'swellCoef']

​    list_filter = ['name']

​    search_fields = ['name']

​    list_per_page = 10



​    \#添加、修改属性

​    \#fields = []

​    \#fieldsets = []

admin.site.register(Oils, OilsAdmin)
```



添加修改属性，下边两者不同一起使用

​    fields = []  

​    fieldsets = []  分组



关联对象：   admin.StackedInline     admin.TabularInline



bool值显示问题： 函数进行值处理，传递函数名

列的显示名称修改： xxx.short_description = "AAAA"



使用装饰器完成注册：@admin.register(Team)



waitress

waitress是一个纯python WSGI服务器，声称具备“非常可接受的性能”。



python 依赖文件

命令自动生成项目相关的依赖

pip freeze > requirements.txt




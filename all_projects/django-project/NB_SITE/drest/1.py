# 设置Django运行锁依赖的环境，demo3为项目文件名，settings是项目的配置文件
import os

if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NB_SITE.settings')

import django

django.setup()

from drest.models import Test

test = Test()
test.save()
test = Test(username='root')
test.save()

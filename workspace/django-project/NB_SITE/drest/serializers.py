from rest_framework import serializers
from drest.models import Test


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        # 此处指明本序列化对应的model
        model = Test
        # 此处指明从model对应数据表中读出哪些字段
        # id字段我们在model中并没指明应该是框架自己创建的
        # 另外我们还创建了created字段，但这里我们不加读取他，当然你要读取加上即可
        fields = ('id', 'username', 'password')

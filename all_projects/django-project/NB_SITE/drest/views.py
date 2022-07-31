# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from drest.serializers import Test
from drest.serializers import TestSerializer


def test(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':  # 这里应该是model对应的所有字段
        test_obj = Test.objects.all()
        # 序列化
        serializer = TestSerializer(test_obj, many=True)
        # 返回
        return JsonResponse(serializer.data, safe=False)

    # 此框架想实现原始REST的思想，如果是post就保存到数据库，这里暂且保留虽然我觉得不实用
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

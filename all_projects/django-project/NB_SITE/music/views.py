# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
import json

from common.change_requests import req


def Index(request):
    return render(request, 'index.html')


# @req
def getJson(request):
    # body = eval(request.body)
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")


def postJson(request):
    body = eval(request.body)
    print(body)
    return HttpResponse(json.dumps(body), content_type="application/json")

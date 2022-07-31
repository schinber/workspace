# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse


def get_girl_pic(request):
    return HttpResponse(u"你好, 美女!!!")

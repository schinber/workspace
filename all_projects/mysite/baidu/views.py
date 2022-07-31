# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
def index(request):
    print("hello world")
    info_dict = {'site': u'百度', 'content': u'搜索引擎'}
    # return render_to_response('index.html', {'info_dict': info_dict})
    return info_dict

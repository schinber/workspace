from flask import Flask, url_for

# url_for 接受两个参数（endpoint,**value）endpoint没有指定就是默认的函数名，根据 view_func.__name__

app = Flask(__name__)


def search_content():
    """search"""
    return {"temp": "你好！！！"}


# url注册的另一种方式
def my_list():
    return '我是列表页'


app.add_url_rule('/list/', endpoint='my_list', view_func=my_list,
                 methods=["POST"])  # 这里endpoint可以不填 ，view_func 一定要是函数名：具体看下面源码解释

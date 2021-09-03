from flask import Flask, url_for

# url_for 接受两个参数（endpoint,**value）endpoint没有指定就是默认的函数名，根据 view_func.__name__
from view import search_content

app = Flask(__name__)


@app.route('/', methods=["POST"])
def hello_world():
    return "Hello World!"


@app.route('/search', methods=["POST"])
def search():
    return search_content()


@app.route('/greeting/<name>', endpoint='say_hello', methods=["POST"])
def give_greeting(name):

    return 'Hello, {0}!'.format(name)


@app.route('/bar', endpoint='bufar')
def bar_view():
    pass


@app.route('/foo')
def foo_view():
    pass


# 请求上下文
with app.test_request_context():
    # print(url_for('foo_view'))  # /foo
    # print(url_for('bufar'))  # /bar
    # # url_for('bar_view') will raise werkzeug.routing.BuildError
    # print(url_for('bar_view'))
    pass
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, abort
from flask import redirect
from admin.url import admin_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.before_request
def before():
    print("我是首先被执行的函数")
    print(f"当前访问的url是{request.path}")
    # print(request.remote_addr)
    if request.remote_addr == '127.0.0.1':
        redirect("/")
        # return '正常请求结果返回'
    else:
        abort(404)


@app.route('/', methods=["GET"])
def hello_world():
    return "Hello World!"


@app.route('/index', methods=["POST"])
def get_rsp():
    body = request.json
    rsp = {"task_id": "0820USN"}
    return rsp


@app.route('/greeting/<name>', endpoint='say_hello', methods=["POST"])
def give_greeting(name):
    return 'Hello, {0}!'.format(name)


@app.route('/bar', endpoint='bufar')
def bar_view():
    pass



app.register_blueprint(admin_blueprint, url_prefix='/admin')
# app.register_blueprint(test_blueprint, url_prefix='/test')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

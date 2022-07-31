# coding:utf-8
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>I am Flask app</h1>"


if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="0.0.0.0", port=5000, debug=True)

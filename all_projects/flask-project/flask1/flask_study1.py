# coding:utf-8
"""
flask 工程练习
"""
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/hello', methods=['GET'])
def hello_world():
    return "Hello World"


@app.route('/index', methods=['POST'])
def hello_index():
    return "Hello index"


if __name__ == '__main__':
    # 启动入口
    app.run(debug=True)

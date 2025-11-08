# coding:utf-8
"""
flask 工程练习
"""
from flask import Flask, request
from views import create_user, delete_user, get_user, get_users, update_user

app = Flask(__name__)


@app.route('/add_user', methods=['POST'])
def add_user():
    # 解析POST请求中的JSON数据
    data = request.get_json()

    # 从请求数据中提取字段，设置默认值
    username = data.get('username')
    email = data.get('email')
    birthdate = data.get('birthdate', None)  # 默认为None
    is_active = data.get('is_active', True)  # 默认为True

    # 调用create_user函数创建用户
    create_user(username=username, email=email, birthdate=birthdate, is_active=is_active)

    return {"status": 0, "message": "User created successfully"}


@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    # 调用delete_user函数删除指定ID的用户
    result = delete_user(user_id=user_id)

    if result:
        return {"status": 0, "message": "User deleted successfully"}
    else:
        return {"status": 1, "message": "User not found or deletion failed"}


@app.route('/index', methods=['GET'])
def hello_world():
    create_user()
    return "Hello World"


@app.route('/list', methods=['POST'])
def hello_index():
    """
    查询所有的用户
    """
    return "Hello index"


@app.route('/username', methods=["POST"])
def list_someone():
    """
    查询某个用户
    """
    return get_user(user_id=None, username=None)


if __name__ == '__main__':
    # 启动入口
    app.run(debug=True)

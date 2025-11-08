# coding:utf-8
"""
flask 工程练习
"""
from flask import Flask
from flask import request
from app.views import delete_user, create_user
from app.views import get_user
from app.views import get_users
from app.views import update_user

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


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    """
    默认页面
    """
    return "Hello World"


@app.route('/list', methods=['GET'])
def hello_index():
    """
    查询所有的用户
    """
    users = get_users()
    return {"status": 0, "data": users}


@app.route('/user_info', methods=["POST"])
def list_someone():
    """
    查询某个用户
    """
    data = request.get_json()
    user_id = data.get('user_id')
    username = data.get('username')
    return get_user(user_id=user_id, username=username)


if __name__ == '__main__':
    # 启动入口
    app.run(port=1111, use_reloader=False)

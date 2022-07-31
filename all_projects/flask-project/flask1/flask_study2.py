# coding:utf-8

from flask import Flask, abort, request, jsonify
from flask import make_response
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

from flask1.models import User

app = Flask(__name__)

# 测试数据暂时存放
tasks = []


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/add_task/', methods=['POST'])
def add_task():
    if not request.json or 'id' not in request.json or 'info' not in request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'info': request.json['info']
    }
    tasks.append(task)
    return jsonify({'result': 'success'})


@app.route('/api/get_task', methods=['GET', 'POST'])
def get_task():
    if not request.args or 'id' not in request.args:
        # 没有指定id则返回全部
        return jsonify(tasks)
    else:
        task_id = request.args['id']
        task = filter(lambda t: t['id'] == int(task_id), tasks)
        return jsonify(task) if task else jsonify({'result': 'not found'})


# 增加
@app.route('/api/insert', methods=['POST'])
def insert_db():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        pwd = data.get('pwd')
    else:
        name = request.args.get("name")
        pwd = request.args.get("pwd")
    user = User(name=name, pwd=pwd)
    db.session.add(user)  # 这个session是临时保存上传数据用的
    db.session.commit()
    json_response = {"status": 200, "message": "success"}
    return jsonify(json_response)


# 删除
@app.route('/api/delete', methods=['POST'])
def delete():
    # 第一种
    user = User.query.order_by(User.id.desc()).first()
    db.session.delete(user)
    db.session.commit()

    # 第二种

    # User.query.filter(User.id='1').delete()
    # db.session.commit()


# 修改
@app.route('/api/change', methods=['POST'])
def change():
    # 第一种
    user = User.query.get(1)
    user.name = 'Python'
    db.session.add(user)
    db.session.commit()

    # 第二种
    # User.query.filter_by(id=1).update({'name': 'python'})
    # db.session.commit()


@app.route('/api/query', methods=['GET', 'POST'])
def query_db():
    User.query.all()  # 查询所有 返回列表
    User.query.first()  # 查询第一个   返回对象
    User.query.get(2)
    query = User.query.all()
    return jsonify({"Hello": "World"})


books = [
    {
        'id': 1,
        'title': u'论语',
        'auther': u'孔子',
        'price': 18
    },
    {
        'id': 2,
        'title': u'道德经',
        'auther': u'老子',
        'price': 15
    }
]


@app.route('/bookstore/api/v1/books', methods=['GET'])
def get_tasks():
    return jsonify({'books': books})


if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/runoob'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config.from_object('models')
    db = SQLAlchemy(app)
    db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)


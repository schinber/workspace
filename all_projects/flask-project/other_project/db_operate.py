"""
复制代码
def query
User.query.all()#查询所有 返回列表
User.query.first() #查询第一个   返回对象
User.query.get(2) #根据主键id获取对象 如果没有则返回None

原生SQLAlchemy查询语句
db.session.query(User).all()
db.session.query(User).first()
db.session.query(User).get(2)

filter_by#只能查查询条件是 =  和and的 其他功能要用filter

User.query.filter_by(id=1)
#<flask_sqlalchemy.BaseQuery object at 0x7f6d9edbb630>
User.query.filter_by(id=1).first()
#<User 1>
User.query.filter_by(id=1).all()
#[<User 1>]
User.query.filter_by(mobile='13911111111', id=1).first()  # and关系

两者区别 filter 里面的参数还要加模型类.属性
　　　　 filter 里的等于是==

filter

User.query.filter(User.mobile=='13911111111').first()

User.query.filter(User.id>10).all()
#[<User 11>, <User 12>, <User 13>, <User 14>, <User 15>, <User 16>...]

from sqlalchemy import or_,not_,and_
User.query.filter(or_(User.id>10,User.mobile=='13173686247')).all()

User.query.filter(User.mobile.startswith('131')).all()

相当于sql语句里的

select * from User where mobile like '131%';

offset
偏移，起始位置

User.query.offset(2).all()
limit
获取限制数据

User.query.limit(3).all()
合起来使用
User.query.offset(6).limit(3).all()
#[<User 7>, <User 8>, <User 9>]

相当于sql语句里的

select * from User limit 6,3;

order_by
排序

复制代码
User.query.order_by(User.id).all()  # 正序
User.query.order_by(User.id.desc()).all()  # 倒序

相当于sql语句中的

select * from User order by id asc;
select * from User order by id desc;
复制代码
优化查询
有的时候我们并不需要查出所有字段 查出的无用数据反而会造成资源浪费

from sqlalchemy.orm import load_only

User.query.options(load_only(User.name,User.mobile)).filter_by(id=1).first()#查询特定字段  options 选项
聚合查询
复制代码
from sqlalchemy import func

db.session.query(表.关注者,func.count(表.被关注者)).group_by(表.关注者)

返回一个列表 [(1,3),(2,4),(4,5)]  ————>一号用户关注了三个 二号用户关注了四个 四号用户关注了五个

#例子 查询用户关注表 中 每个用户关注了几个用户
select 关注者 count(被关注者) from 表 group by 关注者;
复制代码
关联查询
1. 使用ForeignKey
复制代码
class User(db.Model):
    ...
    profile = db.relationship('UserProfile', uselist=False)
    followings = db.relationship('Relation')

class UserProfile(db.Model):
    id = db.Column('user_id', db.Integer, db.ForeignKey('user_basic.user_id'), primary_key=True,  doc='用户ID')
    ...

class Relation(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user_basic.user_id'), doc='用户ID')
    ...

# 测试
user = User.query.get(1)
user.profile.gender
user.followings
复制代码
2. 使用primaryjoin
复制代码
class User(db.Model):
    ...

    profile = db.relationship('UserProfile', primaryjoin='User.id==foreign(UserProfile.id)', uselist=False)
    followings = db.relationship('Relation', primaryjoin='User.id==foreign(Relation.user_id)')

# 测试
user = User.query.get(1)
user.profile.gender
user.followings
复制代码
3. 指定字段关联查询
复制代码
class Relation(db.Model):
    ...
    target_user = db.relationship('User', primaryjoin='Relation.target_user_id==foreign(User.id)', uselist=False)

from sqlalchemy.orm import load_only, contains_eager

Relation.query.join(Relation.target_user).options(load_only(Relation.target_user_id), contains_eager(Relation.target_user).load_only(User.name)).all()


"""

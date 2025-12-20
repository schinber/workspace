from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # 'admin', 'teacher', 'student'
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=True)
    # 新增：头像路径字段（存储相对路径）
    avatar = db.Column(db.String(255), default='default_avatar.png')  # 默认头像

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_admin(self):
        return self.role == 'admin'

    def is_teacher(self):
        return self.role == 'teacher'

    def is_student(self):
        return self.role == 'student'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    student_number = db.Column(db.String(20), unique=True, nullable=False)
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    major = db.Column(db.String(64))
    email = db.Column(db.String(120))
    user = db.relationship('User', backref='student', lazy='dynamic')

    def __repr__(self):
        return f'<Student {self.name}>'
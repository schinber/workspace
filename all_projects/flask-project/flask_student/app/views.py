# from flask import request, jsonify
from app.models import User
from app.models import SESSION


def create_user(username, email, birthdate=None, is_active=True):
    """新增用户"""
    user = User(
        username=username,
        email=email,
        birthdate=birthdate,
        is_active=is_active
    )
    SESSION.add(user)
    SESSION.commit()
    SESSION.refresh(user)  # 刷新获取自增id
    return user


def get_user(user_id=None, username=None):
    """查询用户：支持按id或username查询，返回单个结果"""
    query = SESSION.query(User)
    if user_id:
        return query.filter(User.id == user_id).first()
    if username:
        return query.filter(User.username == username).first()
    return None


def get_users(is_active=True):
    """查询多个用户：默认查询活跃用户"""
    return SESSION.query(User).filter(User.is_active == is_active).all()


def update_user(user_id, **kwargs):
    """修改用户：支持更新username/email/birthdate/is_active，传入需要修改的字段"""
    user = get_user(user_id=user_id)
    if not user:
        return None
    # 更新字段（仅更新传入的参数）
    for key, value in kwargs.items():
        if hasattr(user, key):
            setattr(user, key, value)
    SESSION.commit()
    SESSION.refresh(user)
    return user


def delete_user(user_id):
    """删除用户（物理删除）"""
    user = get_user(user_id=user_id)
    if not user:
        return False
    SESSION.delete(user)
    SESSION.commit()
    return True


def deactivate_user(db, user_id):
    """逻辑删除：将is_active设为False（推荐，保留数据）"""
    return update_user(db, user_id, is_active=False)

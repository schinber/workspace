# 导入必要模块
from functools import wraps
from flask import redirect, url_for, flash, request
from flask_login import current_user
from urllib.parse import urlparse, urljoin


# 权限校验装饰器：仅允许指定角色访问
def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # 1. 先判断是否为匿名用户（会话失效/未登录）
            if not current_user.is_authenticated:  # 匿名用户会返回 False
                # 直接跳转到登录页，携带原访问地址
                return redirect(url_for('main.login', next=request.url))

            # 2. 已登录（非匿名），再做权限校验
            role_check = {
                'admin': current_user.is_admin(),
                'teacher': current_user.is_teacher(),
                'student': current_user.is_student()
            }
            if not role_check.get(role, False):
                flash('权限不足，请使用具有相应权限的账号登录')
                return redirect(url_for('main.login', next=request.url))

            return f(*args, **kwargs)

        return decorated_function

    return decorator


def is_safe_url(target):
    """验证URL是否安全（属于当前应用）"""
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc
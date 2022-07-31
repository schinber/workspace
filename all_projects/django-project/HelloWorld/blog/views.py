from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from django.contrib import auth

# Create your views here.

from django.contrib.auth.backends import ModelBackend
# from .models import UserProfile
#
# # 并集运算
# from django.db.models import Q
#
#
# # 实现用户名邮箱手机号均可登录
# # 继承ModelBackend类，因为它有方法authenticate，可点进源码查看
# class CustomBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因 Q为使用并集查询
#
#             user = UserProfile.objects.get(Q(username=username) | Q(email=username) | Q(mobile=username))
#
#             # django的后台中密码加密：所以不能password==password
#             # UserProfile继承的AbstractUser中有def check_password(self, raw_password):
#
#             if user.check_password(password):
#                 return user
#         except Exception as e:
#             return None
#
#
# def index(request):
#     return render(request, "login.html")
#
#
# def login(request):
#     # 登录提交表单为post
#     if request.method == "POST":
#         # 取不到时为空，username，password为前端页面name值
#         user_name = request.POST.get("username", "")
#         pass_word = request.POST.get("password", "")
#
#         # 成功返回user对象,失败返回null
#         user = auth.authenticate(username=user_name, password=pass_word)
#
#         # 如果不是null说明验证成功
#         if user is not None:
#             # login 两参数：request, user
#             # 实际是对request写了一部分东西进去，这一部分东西其实就是服务端会生成一个sessionID,
#             # 和其对应的用户相关数据信息，将其sessionID与用户相关数据写到数据库中,
#             # 并且将sessionID写到request的cookie中，后期浏览器再发送请求，便将此sessionID发送到Django中,
#             # Django的session中间件再将其获取，并解析出用户user对象赋值给request.user
#             auth.login(request, user)
#             # 跳转到首页 user request会被带回到首页
#             return redirect("/index/")
#     return render(request, "login.html", {})
#
#
# def logout(request):
#     auth.logout(request)
#     return redirect("/login/")

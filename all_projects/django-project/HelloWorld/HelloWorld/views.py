from django.contrib import auth
from django.shortcuts import render, redirect


def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'runoob.html', context)


def page_not_found(request):
    """
    400错误
    :param request:
    :return:
    """
    return render(request, '404.html')


def page_error(request):
    """
    500错误
    :param request:
    :return:
    """
    return render(request, '500.html')


def login(request):
    return render(request, "login.html", {"message": "请输入用户名和密码！"})


def login_check(request):
    if request.method == "GET":
        return render(request, 'login.html')
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")

    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect("/dashboard/")
    else:
        return render(request, "login.html", {"message": "登录名或密码错误！"})


def table(request):
    # 判断登录情况，未登录强制跳转
    if request.user.is_authenticated:
        return render(request, "table.html")
    else:
        return render(request, "login.html", {"message": "请输入用户名和密码！"})


def create_account(request):
    return None


def query(request):
    return
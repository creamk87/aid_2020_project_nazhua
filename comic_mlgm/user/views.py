from django.http import HttpResponse, request
from django.shortcuts import render


# Create your views here.


# 注册
def register_view(request):
    # get请求
    if request.method == "GET":
        return render(request, "user/register.html")
    # post请求
    elif request.method == "POST":
        return HttpResponse("register is ok")

        # username = request.POST.get("username")
        # password_1 = request.POST.get("password1")
        # password_2 = request.POST.get("password2")

        # if not username:
        #     return HttpResponse("please give me username")

        # 检查username是否可用
        # old_users = User.objects.filter(username=username)
        # if old_users:
        #     return HttpResponse("the username is already existed")

        # 密码处理
        # hash算法
        # if password_1 != password_2:
        #     return HttpResponse("the password is not same")

        # hash算法特点
        # 1.定长输出
        # 2.不可逆
        # 3.雪崩效应：输入变化则输出变化
        # m = hashlib.md5()
        # m.update(password_1.encode())
        # password_h = m.hexdigest()

        # try:
        #     user = User.objects.create(username=username, password=password_h)
        # except Exception as e:
        #     print("error is %s" % (e))
        #     return HttpResponse("the username is already existed")


# 登录
def login_view(request):
    # get请求
    if request.method == "GET":
        # 检查cookies和sessions是否已经有过登录记录
        #   如果有,直接跳转登录后页面
        #   如果没有,进入登录页面
        return render(request, "user/login.html")
    # post请求
    elif request.method == "POST":

        return HttpResponse("login is ok")


# 微博第三方登录
def weibo_login_view(request):
    # get请求
    if request == "GET":
        return render(request, "user/weibo_login.html")
    # post请求
    elif request.method == "POST":
        return HttpResponse("Authorized is ok")


# 退出登录
def logout_view(request):
    # 在用户个人中心退出登录后跳转至主页
    return HttpResponse("logout is ok")


# 注销
def delete_view(request):
    # 用户个人中心注销操作后跳转至主页
    return HttpResponse("delete is ok")


# 重置密码
def reset_view(request):
    # get请求
    if request.method == "GET":
        return render(request, "user/reset_passwd.html")
    # post请求
    elif request.method == "POST":
        return HttpResponse("reset is ok")


# 找回密码
def retrieve_view(request):
    # get请求
    if request.method == "GET":
        return render(request, "user/retrieve_passwd.html")
    # post请求
    elif request.method == "POST":
        return HttpResponse("retrieve is ok")

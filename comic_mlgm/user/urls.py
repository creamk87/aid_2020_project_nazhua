from django.urls import path

from user import views

urlpatterns = [
    # 注册：/user/register
    path("register", views.register_view),
    # 登录：/user/login
    path("login", views.login_view),
    # 微博第三方授权登录：/user/weibo_login
    path("weibo_login", views.weibo_login_view),
    # 退出登录：/user/logout
    path("logout", views.logout_view),
    # 注销：/user/delete
    path("delete", views.delete_view),
    # 主动重置密码/忘记密码重置：/user/reser_passwd
    path("reset_passwd", views.reset_view),
    # 忘记密码,找回密码：/user/retrieve_passwd
    path("retrieve_passwd", views.retrieve_view),
]

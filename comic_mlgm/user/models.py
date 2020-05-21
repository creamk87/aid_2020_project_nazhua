from django.db import models

# Create your models here.

# 用户注册登录表
# class Users(models.Model):
#     User_Name = models.CharField("用户名", max_length=30, unique=True,primary_key=True)
#     Password = models.CharField("密码", max_length=32)
#     User_Email= models.EmailField("邮箱", max_length=30, unique=True)
#     Authorization_Status=models.BooleanField("是否获得第三方授权")
#     Login_Status=models.BooleanField("登录状态")
#     Created_Time = models.DateTimeField('创建时间', auto_now_add=True)
#     Updated_Time = models.DateTimeField('更新时间', auto_now=True)
#
# # 用户个人信息表
# class User_Profile(models.Model):
#     Nick_Name = models.CharField("昵称", max_length=30, unique=True,primary_key=True)
#     User_Type = models.CharField("用户类型", max_length=30, unique=True,primary_key=True)
#     Vip_Rank=models.CharField("会员等级", max_length=30, unique=True,primary_key=True)
    # Moderator_id=
    # Administrater_id=
    # Age=
    # Career=
    # User_Addr=
    # Gender=
    # Birth=
    # Portrait=
    # Created_Time=models.DateTimeField('创建时间', auto_now_add=True)
    # Updated_Time=models.DateTimeField('更新时间', auto_now=True)


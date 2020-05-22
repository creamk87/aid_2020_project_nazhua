from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('rename', views.rename),
    path('new', views.new),
]

from django.contrib import admin
from django.urls import path, include

from index import views

urlpatterns = [
    # http://127.0.0.1:8000/index
    path('', views.index),
    path('details', views.details),
]
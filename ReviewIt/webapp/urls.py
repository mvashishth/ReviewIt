from django.urls import path

from . import views

urlpatterns = [
    path('', views.upload_file),
    path('webapp/', views.yolo, name="yolo"),
    path('webapp/', views.super_res, name="super_res"),
]
"""rpiCVapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from face_detection.views import FaceDetection

urlpatterns = [
    path('admin/', admin.site.urls),
    # 目前urls.py里path和re_path都只能指向视图view里的一个函数或方法，
    # 而不能指向一个基于类的视图(Class Based View)。Django提供了一个额外as_view()方法，
    # 可以将一个类伪装成方法。这点在当你使用Django在带的view类或自定义的类时候非常重要
    path('',FaceDetection.as_view(),name='home'),
    # call a method in the view.py
    path('facedetection/',FaceDetection.detect,name='detect')
]

"""wil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import insert_into_database

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('area_button_click/', views.area_button_click, name='area_button_click'),
    path('location/', views.location, name='location'),
    path('timer/', views.timer, name='timer'),
    path('timer/', views.timer_view, name='timer'),
    path('insert-into-database/', insert_into_database, name='insert_into_database'),
    path('login/', views.login, name='login'),

]

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
from . import views

urlpatterns = [
    path('wiladmin/', views.AdminLoginController.as_view(), name='index'),
    path('wiladmin/login', views.AdminLoginController.as_view(), name='adminlogin'),
    path('wiladmin/dashboard', views.AdminDashboardController.as_view(), name='admindashboard'),
    path('wiladmin/logs', views.AdminReportLogsController.as_view(), name='reportlogs'),
    path('wiladmin/walkindashboard', views.AdminWalkinDashboardController.as_view(), name='walkindashboard'),
    path('wiladmin/updatebooking/<int:bookingid>', views.AdminWalkinDashboardController.as_view(), name='updatebooking'),
    path('wiladmin/deletebooking/<int:bookingid>', views.AdminWalkinDashboardController.as_view(), name='deletebooking'),
    path('wiladmin/bookguest', views.BookGuestController.as_view(), name='bookguest'),
]

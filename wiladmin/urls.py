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
from django.urls import path
from . import views

urlpatterns = [
    path('wiladmin/', views.AdminLoginController.as_view(), name='index'),
    path('wiladmin/login', views.AdminLoginController.as_view(), name='adminlogin'),
    path('wiladmin/logout', views.handleLogout, name='adminlogout'),
    path('wiladmin/admindashboard', views.AdminDashboardController.as_view(), name='admindashboard'),
    path('wiladmin/reportlogs', views.AdminReportLogsController.as_view(), name='reportlogs'),
    path('wiladmin/walkindashboard', views.AdminWalkinDashboardController.as_view(), name='walkindashboard'),
    path('wiladmin/reserveddashboard', views.AdminReservedDashboardController.as_view(), name='reserveddashboard'),
    path('wiladmin/updatebooking/<int:bookingid>', views.AdminWalkinDashboardController.as_view(), name='updatebooking'),
    path('wiladmin/deletebooking/<int:bookingid>', views.AdminWalkinDashboardController.as_view(), name='deletebooking'),
    path('wiladmin/updatereserved/<int:reserved_id>', views.AdminReservedDashboardController.as_view(), name='updatereserved'),
    path('wiladmin/deletereserved/<int:reserved_id>', views.AdminReservedDashboardController.as_view(), name='deletereserved'),
    path('wiladmin/bookguest', views.BookGuestController.as_view(), name='bookguest'),
    path('wiladmin/workspaces', views.ViewWorkspacesController.as_view(), name='workspaces'),
    path('wiladmin/workspaces/<str:areaid>', views.ViewWorkspacesController.as_view(), name='usersinarea'),
    path('wiladmin/test', views.TestController.as_view(), name='test'),
    path('wiladmin/test/<str:areaid>', views.TestController.as_view(), name='testusers'),
]


from django.urls import path
from .views import insert_into_database, show_message_view
from django.contrib import admin
from . import views
from . import user_login_controller
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('map/', views.map, name='map'),
    path('area_button_click/', views.area_button_click, name='areaButtonClick'),
    path('location/', views.location, name='location'),
    path('activebooking/', views.ActiveBookingController.as_view(), name='activebooking'),
    path('timer/', views.timer, name='timer'),
    path('insert-into-database/', insert_into_database, name='insertIntoDatabase'),
    path('show_message/', show_message_view, name='show_message'),
    path('userlogin/', user_login_controller.UserLoginController.as_view(), name='user_login'),
    path('userlogout/', views.user_logout, name='user_logout'),
    path('userdashboard/', views.user_dashboard, name='user_dashboard'),
    path('userprofile/', views.user_profile, name='userprofile'),
    path('admin/', admin.site.urls),
    path('get_timer_data/', views.get_timer_data, name='get_timer_data'),
    path('end_session/', views.end_session_view, name='end_session'),
    path('get-booking-info/', views.get_booking_info, name='get_booking_info'),
    path('get-reservebooking-info/', views.get_reservebooking_info, name='get_reservebooking_info'),
    path('get-calendar-data/', views.get_calendar_data, name='get_calendar_data'),
    
]

  
    
    
    
      
    
    
    
    
   


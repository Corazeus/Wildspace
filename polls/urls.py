
from django.urls import path
from .views import insert_into_database, show_message_view

from . import views


urlpatterns = [
    
    path('', views.index, name='index'),
    path('area_button_click/', views.area_button_click, name='areaButtonClick'),
    path('location/', views.location, name='location'),
    path('timer/', views.timer, name='timer'),
    path('insert-into-database/', insert_into_database, name='insertIntoDatabase'),
    path('show_message/', show_message_view, name='show_message'),

]

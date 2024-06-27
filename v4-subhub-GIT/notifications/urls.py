from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.notifications_view, name='notifications'),
    path('notifications/new/', views.new_notification_view, name='new_notification'),
    path('notifications/update/<int:pk>/', views.update_notification_view, name='update_notification'),
    path('notifications/all/', views.all_notifications_view, name='notifications_list'),
    path('notifications/detail/<int:pk>/', views.notification_detail, name='detail'),
    path('notifications/search', views.search_noti, name='search_noti'),
]
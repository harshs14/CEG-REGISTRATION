from django.urls import re_path, path
from . import views

urlpatterns = [
    path('event/', views.Events.as_view(), name='event_list'),
    path('event/<int:pk>/', views.EventDetail.as_view(), name='detail'),
    path('event/<int:pk>/register', views.EventRegister.as_view(), name='register'),
]


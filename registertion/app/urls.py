from django.urls import re_path, path
from . import views

urlpatterns = [
    path('event/', views.Events.as_view(), name='event_list'),
]

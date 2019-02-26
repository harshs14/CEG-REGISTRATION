from django.urls import re_path, path
from . import views

urlpatterns = [
    path('event/', views.Events.as_view(), name='event_list'),
    # path('event/(?P<e_id>[0-9]+)/', views.EventDetail.as_view(), name='event_detail'),
    path('event/<int:pk>/', views.EventDetail.as_view(), name='detail'),
]


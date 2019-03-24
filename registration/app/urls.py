from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^event/$', views.Events.as_view(), name='event_list'),
    re_path(r'^event/(?P<e_id>[0-9]+)/$', views.EventDetail.as_view(), name='detail'),
    re_path(r'^event/(?P<e_id>[0-9]+)/register/$', views.EventRegister.as_view(), name='register'),
    re_path(r'^contact/$', views.Contact.as_view(), name='contact'),
]

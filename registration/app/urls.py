from django.urls import re_path, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^event/$', views.Events.as_view(), name='event_list'),
    re_path(r'^event/(?P<e_id>[0-9]+)/$', views.EventDetail.as_view(), name='detail'),
    re_path(r'^event/(?P<e_id>[0-9]+)/register/$', views.EventRegister.as_view(), name='register'),
    re_path(r'^contact/$', views.Contact.as_view(), name='contact'),
    re_path(r'^ajax_calls/search/', views.autocompleteModel),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

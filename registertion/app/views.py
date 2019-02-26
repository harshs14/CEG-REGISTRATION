from django.views import View
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404


class Events(View):
    template_name = 'app/event.html'

    def get(self, request, *args, **kwargs):
        context = {
            'event_list': Event.objects.order_by('id'),
        }
        return render(request, self.template_name, context)


class EventDetail(View):
    template_name = 'app/event_detail.html'

    def get(self, request, *args, **kwargs):

        event_obj = Event.objects.get(pk=kwargs['pk'])
        context = {
            'name': event_obj.name,
            'description': event_obj.description,
            'venue': event_obj.venue,
            'avatar': event_obj.avatar,
            'video': event_obj.video,
            'time': event_obj.timestamp,
            'seats': event_obj.seats,
            'id': event_obj.id,
          }



        return render(request, self.template_name, context)








from django.views import View
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from registertion.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string


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


class EventRegister(View):
    template_name = 'app/event_register.html'

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        event_obj = Event.objects.get(pk=kwargs['pk'])

        form = RegisterForm(request.POST)
        if form.is_valid():
            event_register = form.save(commit=False)
            event_register.event_id = event_obj
            event_register.event_name = event_obj.name
            event_register.save()
            print(event_register.email, "2")
            x = event_obj.name
            r_id = event_register
            message = "YOU ARE SUCCESSFULLY REGISTERED FOR THE EVENT->" + str(x) + ". \n REGISTRATION ID->" + str(r_id)
            # message = "REGISTERED"
            subject = "CEG EVENT REGISTRATION"
            from_mail = EMAIL_HOST_USER
            to_mail = [event_register.email]
            send_mail(subject, message, from_mail, to_mail, fail_silently=False)
            # messages.success(request, 'VERIFY YOUR EMAIL.')

        return render(request, 'app/registered.html')

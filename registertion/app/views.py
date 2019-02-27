from django.views import View
from .models import *
from .forms import *
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
            print(form, "1")
            print(event_register, "2")

        # message = render_to_string('app/event_register_email.html', {
        #
        #
        # })
        # from_mail = EMAIL_HOST_USER
        # to_mail = [user.email]
        # send_mail(subject, message, from_mail, to_mail, fail_silently=False)
        # messages.success(request, 'VERIFY YOUR EMAIL.')

        return render(request, 'app/registered.html')

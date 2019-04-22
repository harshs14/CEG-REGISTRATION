from django.contrib import messages
from django.views import View
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from registration.settings import EMAIL_HOST_USER
import json
import urllib
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse


class Events(View):
    template_name = 'app/event.html'

    def get(self, request, *args, **kwargs):
        context = {
            'event_list': Event.objects.order_by('id'),
        }
        return render(request, self.template_name, context)


class EventDetail(View):
    template_name = 'app/event_detail.html'

    def get(self, request, e_id, *args, **kwargs):

        event_obj = Event.objects.get(pk=e_id)
        context = {
            'event': Event.objects.filter(pk=e_id),
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

    def get(self, request, e_id, *args, **kwargs):
        form = RegisterForm()
        event_obj = Event.objects.filter(pk=e_id)
        event = Event.objects.get(pk=e_id)
        if event.seats == 0:
            return render(request, 'app/seats_full.html')
        else:
            context = {'form': form, 'event': event_obj}
            return render(request, self.template_name, context)

    def post(self, request, e_id, *args, **kwargs):

        event_obj = Event.objects.get(pk=e_id)

        form = RegisterForm(request.POST)
        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                form.save()
                messages.success(request, 'successful registration!')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

            event_register = form.save(commit=False)
            event_register.event_id = event_obj
            event_register.event_name = event_obj.name
            event_obj.seats = event_obj.seats - 1
            event_obj.save()
            event_register.save()
            print(event_register.email, "2")
            x = event_obj.name
            r_id = event_register
            message = "YOU ARE SUCCESSFULLY REGISTERED FOR THE EVENT->" + str(x) + ".\nREGISTRATION ID->" + str(r_id)
            subject = "CEG EVENT REGISTRATION"
            from_mail = EMAIL_HOST_USER
            to_mail = [event_register.email]
            send_mail(subject, message, from_mail, to_mail, fail_silently=False)
            messages.success(request, "SUCCESSFULLY REGISTERED")
        return redirect('event_list')


class Contact(View):
    template_name = 'app/contact_us.html'

    def get(self, request, *args, **kwargs):

        form = ContactForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):

        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()

            message = "THANK YOU FOR CONTACTING CEG, YOUR ENQUIRY WILL BE RESOLVED SOON"
            subject = "CONTACT CEG"
            from_mail = EMAIL_HOST_USER
            to_mail = [contact.email]
            send_mail(subject, message, from_mail, to_mail, fail_silently=False)
        return render(request, 'app/contact_done.html')


def autocompleteModel(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        search_qs = Event.objects.filter(name__startswith=q)
        results = []
        print(q)
        for r in search_qs:
            results.append(r.name)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
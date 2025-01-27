from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Event(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True)
    description = models.CharField(max_length=1000, null=False, blank=True)
    avatar = models.ImageField(upload_to='event_pic', null=True, blank=True)
    video = models.FileField(upload_to='event_video', null=True, blank=True)
    venue = models.CharField(max_length=100, null=False, blank=True)
    timestamp = models.DateTimeField(default=None, null=True)
    seats = models.IntegerField(null=False, blank=True)

    def __str__(self):
        return str(self.id)


class Register(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    phone_number = PhoneNumberField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    address = models.CharField(null=False, blank=False, max_length=200)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100, null=False, blank=True)

    def __str__(self):
        return str(self.id)


class Contact(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone_number = PhoneNumberField(blank=False, null=False)
    enquiry = models.CharField(max_length=500, blank=False, null=False)

    def __str__(self):
        return str(self.id)

from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField


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

    STATE_CHOICE = (
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh','Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh','Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Orissa', 'Orissa'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telagana', 'Telagana'),
        ('Tripura', 'Tripura'),
        ('Uttaranchal', 'Uttaranchal'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('West Bengal', 'West Bengal'),
        ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
        ('Chandigarh', 'Chandigarh'),
        ('Dadar and Nagar Haveli', 'Dadar and Nagar Haveli'),
        ('Daman and Diu', 'Daman and Diu'),
        ('Delhi', 'Delhi'),
        ('Lakshadeep', 'Lakshadeep'),
        ('Pondicherry', 'Pondicherry')
    )

    CATEGORY_CHOICE = (
        ('Govt', 'Govt'),
        ('Private', 'Private')
    )

    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )

    first_name = models.CharField(max_length=50, null=False, blank=False)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    gender = models.CharField(max_length=50, blank=True,null=True, choices=GENDER_CHOICE)
    email = models.EmailField(null=False, blank=False)
    address = models.CharField(null=False, blank=False, max_length=200)
    city = models.CharField(null=False, blank=False, max_length=50)
    state = models.CharField(max_length=50, blank=True,null=True, choices=STATE_CHOICE)
    pincode = models.IntegerField(blank=False, null=False)
    category = models.CharField(max_length=50, blank=True, null=True, choices=CATEGORY_CHOICE)
    organisation = models.CharField(max_length=50, null=False, blank=False)
    designation = models.CharField(max_length=50, null=False, blank=False)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100, null=False, blank=True)
    # captcha = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.id)


class Contact(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    enquiry = models.CharField(max_length=500, blank=False, null=False)

    def __str__(self):
        return str(self.id)

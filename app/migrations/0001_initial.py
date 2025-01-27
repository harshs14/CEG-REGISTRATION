# Generated by Django 2.1.5 on 2019-06-17 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('enquiry', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='event_pic')),
                ('video', models.FileField(blank=True, null=True, upload_to='event_video')),
                ('venue', models.CharField(blank=True, max_length=100)),
                ('timestamp', models.DateTimeField(default=None, null=True)),
                ('seats', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Orissa', 'Orissa'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telagana', 'Telagana'), ('Tripura', 'Tripura'), ('Uttaranchal', 'Uttaranchal'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadar and Nagar Haveli', 'Dadar and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Delhi', 'Delhi'), ('Lakshadeep', 'Lakshadeep'), ('Pondicherry', 'Pondicherry')], max_length=50, null=True)),
                ('pincode', models.IntegerField()),
                ('category', models.CharField(blank=True, choices=[('Govt', 'Govt'), ('Private', 'Private')], max_length=50, null=True)),
                ('organisation', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('event_name', models.CharField(blank=True, max_length=100)),
                ('captcha', models.IntegerField()),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Event')),
            ],
        ),
    ]

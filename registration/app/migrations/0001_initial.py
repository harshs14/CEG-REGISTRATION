# Generated by Django 2.1.5 on 2019-03-31 14:49

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


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
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
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
                ('name', models.CharField(blank=True, max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('event_name', models.CharField(blank=True, max_length=100)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Event')),
            ],
        ),
    ]

# Generated by Django 2.1.5 on 2019-06-17 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='captcha',
        ),
    ]
# Generated by Django 2.1.5 on 2019-06-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_register_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50),
        ),
    ]

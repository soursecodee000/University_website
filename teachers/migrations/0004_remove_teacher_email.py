# Generated by Django 3.0.3 on 2020-08-29 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_auto_20200827_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='email',
        ),
    ]

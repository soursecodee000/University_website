# Generated by Django 5.0.3 on 2024-09-08 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0003_auto_20200827_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='departmentimages',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

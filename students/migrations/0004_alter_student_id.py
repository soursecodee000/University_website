# Generated by Django 5.0.3 on 2024-09-08 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_remove_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

# Generated by Django 4.2.5 on 2024-03-31 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Home_App", "0027_remove_user_registration_student_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="student", name="user",),
    ]

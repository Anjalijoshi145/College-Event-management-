# Generated by Django 4.2.5 on 2024-03-30 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Home_App", "0022_user_registration_user_alter_user_registration_name"),
    ]

    operations = [
        migrations.RemoveField(model_name="user_registration", name="user",),
        migrations.DeleteModel(name="Student",),
    ]

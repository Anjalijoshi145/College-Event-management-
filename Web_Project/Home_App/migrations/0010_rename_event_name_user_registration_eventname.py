# Generated by Django 4.2.5 on 2024-03-24 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Home_App", "0009_alter_user_registration_event_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user_registration", old_name="event_name", new_name="eventname",
        ),
    ]

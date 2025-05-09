# Generated by Django 4.2.5 on 2024-03-29 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Home_App", "0021_remove_user_registration_student_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user_registration",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="user_registration",
            name="name",
            field=models.CharField(max_length=200, null=True),
        ),
    ]

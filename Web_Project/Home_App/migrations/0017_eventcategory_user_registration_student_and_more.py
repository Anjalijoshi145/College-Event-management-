# Generated by Django 4.2.5 on 2024-03-28 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Home_App", "0016_student_date_created_student_email_student_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="user_registration",
            name="student",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Home_App.student",
            ),
        ),
        migrations.AddField(
            model_name="user_registration",
            name="category",
            field=models.ManyToManyField(to="Home_App.eventcategory"),
        ),
    ]

# Generated by Django 3.2.20 on 2023-09-25 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Question",
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
                (
                    "questions_regarding",
                    models.CharField(
                        choices=[
                            ("ORDER", "the order"),
                            ("DELIVERT", "the delivery"),
                            ("RETURN", "returning an order"),
                            ("PAYMENT", "the payment"),
                            ("ACCOUNT", "my account"),
                            ("NEWSLETTER", "the newsletter subscription"),
                            ("OTHER", "other"),
                        ],
                        default="O",
                        max_length=254,
                    ),
                ),
                (
                    "your_question",
                    models.TextField(default="", max_length=500),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Answer",
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
                ("answer", models.TextField(default="", max_length=500)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="question",
                        to="help_center.question",
                    ),
                ),
                (
                    "responder",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="responder",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

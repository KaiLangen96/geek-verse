# Generated by Django 3.2.20 on 2023-09-30 11:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_auto_20230907_1608"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="rating",
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(5),
                ]
            ),
        ),
    ]

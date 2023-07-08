# Generated by Django 4.2.3 on 2023-07-08 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("words", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExampleModel",
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
                ("sentence", models.TextField()),
                ("translation", models.TextField()),
                (
                    "word",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="words.wordmodel",
                    ),
                ),
            ],
        ),
    ]
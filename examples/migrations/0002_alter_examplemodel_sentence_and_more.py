# Generated by Django 4.2.3 on 2023-07-09 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("examples", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="examplemodel",
            name="sentence",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="examplemodel",
            name="translation",
            field=models.TextField(blank=True),
        ),
    ]

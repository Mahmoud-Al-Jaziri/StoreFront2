# Generated by Django 4.2.7 on 2023-11-21 16:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0003_add_slug_to_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="adress",
            name="zip",
            field=models.CharField(default="00000", max_length=10),
        ),
    ]

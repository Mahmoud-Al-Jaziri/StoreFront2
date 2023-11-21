# Generated by Django 4.2.7 on 2023-11-21 16:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0004_adress_zip"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="customer",
            index=models.Index(
                fields=["last_name", "first_name"],
                name="store_custo_last_na_2e448d_idx",
            ),
        ),
    ]

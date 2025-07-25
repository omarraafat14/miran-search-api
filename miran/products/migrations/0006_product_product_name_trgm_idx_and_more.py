# Generated by Django 4.2 on 2025-05-24 13:34

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_enable_trigram_extension"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="product",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["name"],
                name="product_name_trgm_idx",
                opclasses=["gin_trgm_ops"],
            ),
        ),
        migrations.AddIndex(
            model_name="product",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["name_ar"],
                name="product_name_ar_trgm_idx",
                opclasses=["gin_trgm_ops"],
            ),
        ),
    ]

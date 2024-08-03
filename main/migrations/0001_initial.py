# Generated by Django 5.0.6 on 2024-08-03 19:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GeneralItem",
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
                ("purchased_at", models.DateTimeField(auto_now_add=True)),
                (
                    "purchase_place",
                    models.CharField(blank=True, max_length=1024, null=True),
                ),
                ("photo", models.ImageField(upload_to="images/")),
                ("quantity", models.IntegerField(blank=True, null=True)),
                ("price", models.IntegerField(blank=True, null=True)),
                ("comments", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="ApplianceItem",
            fields=[
                (
                    "generalitem_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="main.generalitem",
                    ),
                ),
                ("warranty_expiration", models.DateField()),
            ],
            bases=("main.generalitem",),
        ),
        migrations.CreateModel(
            name="ClothingItem",
            fields=[
                (
                    "generalitem_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="main.generalitem",
                    ),
                ),
                ("size", models.CharField(max_length=10)),
                ("color", models.CharField(max_length=50)),
            ],
            bases=("main.generalitem",),
        ),
        migrations.CreateModel(
            name="FoodItem",
            fields=[
                (
                    "generalitem_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="main.generalitem",
                    ),
                ),
                ("expiration_date", models.DateField()),
            ],
            bases=("main.generalitem",),
        ),
        migrations.CreateModel(
            name="FurnitureItem",
            fields=[
                (
                    "generalitem_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="main.generalitem",
                    ),
                ),
                ("dimensions", models.CharField(max_length=100)),
            ],
            bases=("main.generalitem",),
        ),
        migrations.CreateModel(
            name="Location",
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
                ("name", models.CharField(max_length=256)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="main.location",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="generalitem",
            name="location",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="main.location",
            ),
        ),
        migrations.CreateModel(
            name="PriceHistory",
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
                ("price", models.IntegerField()),
                ("date_recorded", models.DateTimeField(auto_now_add=True)),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.generalitem",
                    ),
                ),
            ],
        ),
    ]

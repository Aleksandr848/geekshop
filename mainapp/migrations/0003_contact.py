# Generated by Django 3.2.12 on 2022-03-05 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0002_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("phone", models.CharField(max_length=50, verbose_name="номер телефона")),
                ("email", models.EmailField(max_length=254, verbose_name="электронная почта")),
                ("city", models.CharField(default="Москва", max_length=128, verbose_name="город")),
                ("address", models.CharField(max_length=254, verbose_name="адресс")),
            ],
        ),
    ]

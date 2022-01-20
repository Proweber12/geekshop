# Generated by Django 3.2.10 on 2022-01-04 15:16

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
                ("city", models.CharField(default="Москва", max_length=128, verbose_name="город")),
                ("phone", models.CharField(max_length=50, verbose_name="номер телефона")),
                ("email", models.EmailField(max_length=254, verbose_name="электронная почта")),
                ("address", models.CharField(max_length=254, verbose_name="адрес")),
            ],
        ),
    ]
# Generated by Django 4.1.11 on 2023-09-24 10:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoices", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
# Generated by Django 4.1.3 on 2022-12-10 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user", name="age", field=models.IntegerField(null=True),
        ),
    ]
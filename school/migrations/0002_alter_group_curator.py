# Generated by Django 4.2.7 on 2023-11-05 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="curator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="groups",
                to="school.teacher",
            ),
        ),
    ]

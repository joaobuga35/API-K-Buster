# Generated by Django 4.2 on 2023-04-16 18:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("movies_orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movieorder",
            name="buyed_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]

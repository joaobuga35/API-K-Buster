# Generated by Django 4.2 on 2023-04-16 18:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies_orders", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movies", "0003_rename_movies_movie"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="orders",
            field=models.ManyToManyField(
                related_name="movie_orders",
                through="movies_orders.MovieOrder",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
from django.db import models


# Create your models here.
class CategoryMovie(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20,
        null=True,
        choices=CategoryMovie.choices,
        default=CategoryMovie.G,
    )
    synopsis = models.TextField(null=True, default=None)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )
    orders = models.ManyToManyField(
        "users.User", through="movies_orders.MovieOrder", related_name="movie_orders"
    )

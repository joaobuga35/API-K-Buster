from django.db import models

# Create your models here.


class MovieOrder(models.Model):
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="movie_orders"
    )

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_movie_orders"
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    buyed_at = models.DateTimeField(auto_now_add=True)

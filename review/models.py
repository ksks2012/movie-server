from django.contrib.auth.models import User
from django.db import models


class Review(models.Model):
    class Meta:
        db_table = 'review'

    # relation
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='reviews',
        null=True
    )
    movie = models.ForeignKey(
        'movie.Movie',
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    # own
    text = models.TextField()
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
    )

    # meta
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

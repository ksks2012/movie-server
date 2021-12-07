from django.db import models


class Movie(models.Model):
    class Meta:
        db_table = 'movie'

    # relation
    #
    # own
    title = models.TextField()
    year = models.IntegerField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0
    )
    genres = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)

    # meta
    is_yts = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

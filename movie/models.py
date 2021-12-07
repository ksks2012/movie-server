from django.db import models


class Movie(models.Model):
    class Meta:
        db_table = 'movie'

    # relation
    #
    # own
    title = models.TextField()
    year = models.IntegerField()
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
    )
    genres = models.CharField(max_length=30, blank=True, null=True)
    summary = models.TextField()

    # meta
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

from django.db import models
from django.contrib.auth.models import User


class ReviewVote(models.Model):
    class Meta:
        db_table = 'review_vote'
        constraints = [
            models.UniqueConstraint(fields=['user', 'review'], name='unique_review_vote')
        ]

    # relation
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='votes',
        null=True
    )
    review = models.ForeignKey(
        'review.Review',
        on_delete=models.CASCADE,
        related_name='votes'
    )
    # own
    # -
    # meta
    created_at = models.DateTimeField(auto_now_add=True)

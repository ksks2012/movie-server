from rest_framework import serializers

from vote.models import ReviewVote


class ReviewVoteSerializer(serializers.ModelSerializer):
    review_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ReviewVote
        fields = (
            'id',
            'review_id',
            'created_at',
        )

from rest_framework import serializers

from review.models import Review
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

    def validate_review_id(self, review_id):
        try:
            Review.objects.get(id=review_id)
            return review_id
        except Review.DoesNotExist:
            raise serializers.ValidationError('Does Not Exists.')

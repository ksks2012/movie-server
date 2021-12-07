from rest_framework import serializers

from review.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    movie_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Review
        fields = (
            'id',
            'movie_id',
            'text',
            'rating',
            'created_at',
            'updated_at',
        )

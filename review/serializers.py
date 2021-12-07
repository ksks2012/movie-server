from rest_framework import serializers

from review.models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = (
            'id',
            'text',
            'rating',
            'created_at',
            'updated_at',
        )

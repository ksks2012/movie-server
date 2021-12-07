from rest_framework import serializers

from movie.models import Movie
from review.serializers import ReviewSerializer


class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)

    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'year',
            'rating',
            'genres',
            'summary',
        )


class MovieDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'year',
            'rating',
            'genres',
            'summary',
            'reviews',
        )

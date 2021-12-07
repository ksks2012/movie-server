from rest_framework import serializers

from movie.models import Movie
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
            'count_vote',
            'created_at',
            'updated_at',
        )

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
            return movie_id
        except Movie.DoesNotExist:
            raise serializers.ValidationError('Does Not Exists.')

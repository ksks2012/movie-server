from django.db.models import Avg

from movie.models import Movie
from review.models import Review


class ReviewService:
    def _update_movie_rating(self, movie: Movie):
        updated_rating = Review.objects.filter(movie=movie) \
            .aggregate(rating=Avg('rating'))['rating']
        movie.rating = updated_rating
        movie.save()

    def create(self, user, **validated_data):
        review = Review.objects.create(user=user, **validated_data)
        movie = review.movie
        self._update_movie_rating(movie)
        return review

    def update(self, review: Review, data):
        text = data.get('text')
        if text is not None:
            review.text = text
        rating = data.get('rating')
        if rating is not None:
            review.rating = rating
        review.save()
        if rating is not None:
            movie = review.movie
            self._update_movie_rating(movie)
        return review

    def delete(self, review: Review):
        movie = review.movie
        review.delete()
        self._update_movie_rating(movie)

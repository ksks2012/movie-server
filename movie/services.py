from movie.models import Movie


class MovieService:
    def create(self, **validated_data):
        movie = Movie.objects.create(**validated_data)
        return movie

    def filter_and_order_movies(self, query_params):
        movies = Movie.objects.all()
        year = query_params.get('year')
        genres = query_params.get('genres')
        title = query_params.get('title')
        ordering_option = query_params.get('ordering')

        filter_options = dict()
        if year is not None:
            filter_options['year'] = year
        if genres is not None:
            filter_options['genres__icontains'] = genres
        if title is not None:
            filter_options['title__icontains'] = title
        filtered_movies = movies.filter(**filter_options)

        if ordering_option in ['-rating', 'rating']:
            filtered_movies = filtered_movies.order_by(ordering_option)

        return filtered_movies

from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from movie.filters import MovieFilter
from movie.models import Movie
from movie.serializers import MovieSerializer, MovieDetailSerializer


class MovieViewSet(viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]

    def list(self, request):
        """
        영화 리스트 조회
        - GET /movies/
        """
        filtered_movies = MovieFilter().filter_queryset(request, Movie.objects.all())
        paginated_movies = self.paginate_queryset(filtered_movies)

        rtn = MovieSerializer(paginated_movies, many=True).data
        return self.get_paginated_response(rtn)

    def retrieve(self, request, pk):
        """
        영화 디테일 조회
        - GET /movies/{movie_id}/
        """
        try:
            movie = Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            return Response({"error": "Does not Exists."}, status=status.HTTP_404_NOT_FOUND)

        rtn = MovieDetailSerializer(movie).data
        return Response(rtn, status=status.HTTP_200_OK)

    def create(self, request):
        """
        영화 생성
        - POST /movies/
        """
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie = Movie.objects.create(**serializer.validated_data)

        rtn = MovieSerializer(movie).data
        return Response(rtn, status=status.HTTP_201_CREATED)

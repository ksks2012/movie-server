from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from movie.models import Movie
from movie.serializers import MovieSerializer, MovieDetailSerializer


class MovieViewSet(viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    permission_classes = [AllowAny]
    serializer_class = MovieSerializer
    def list(self, request):
        """
        영화 리스트 조회
        - GET /movies/
        """
        movies = Movie.objects.all()
        return self.get_paginated_response(MovieSerializer(self.paginate_queryset(movies), many=True).data)

    def retrieve(self, request, pk):
        """
        영화 디테일 조회
        - GET /movies/{movie_id}/
        """
        try:
            movie = Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            return Response({"error": "Does not Exists."}, status=status.HTTP_404_NOT_FOUND)
        return Response(MovieDetailSerializer(movie).data, status=status.HTTP_200_OK)

    def create(self, request):
        """
        영화 생성
        - POST /movies/
        """
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie = Movie.objects.create(**serializer.validated_data)
        return Response(MovieSerializer(movie).data, status=status.HTTP_201_CREATED)

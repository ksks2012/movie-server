from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class MovieViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        """
        영화 리스트 조회
        - GET /movies/
        """
        pass

    def retrieve(self, request, pk):
        """
        영화 디테일 조회
        - GET /movies/{movie_id}/
        """
        pass

    def create(self, request):
        """
        영화 생성
        - POST /movies/
        """
        pass

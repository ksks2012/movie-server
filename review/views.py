from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class ReviewViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]

    def retrieve(self, request, pk):
        """
        영화 리뷰 디테일 조회
        - GET /review/{review_id}/
        """
        pass

    def create(self, request):
        """
        영화 리뷰 생성
        - POST /reviews/
        """
        pass

    def update(self, request, pk):
        """
        영화 리뷰 수정
        - PUT /reviews/{review_id}/
        """
        pass

    def delete(self, request, pk):
        """
        영화 리뷰 삭제
        - DELETE /reviews/{review_id}/
        """
        pass

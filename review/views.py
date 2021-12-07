from django.db import transaction
from rest_framework import status, viewsets

from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from review.models import Review
from review.serializers import ReviewSerializer
from review.services import ReviewService


class ReviewViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated()]

    def get_permissions(self):
        if self.action in ('retrieve',):
            return [AllowAny()]
        return self.permission_classes

    def retrieve(self, request, pk):
        """
        영화 리뷰 디테일 조회
        - GET /review/{review_id}/
        """
        try:
            review = Review.objects.get(id=pk)
        except Review.DoesNotExist:
            return Response({"error": "Does not Exists."}, status=status.HTTP_404_NOT_FOUND)

        rtn = ReviewSerializer(review).data
        return Response(rtn, status=status.HTTP_200_OK)

    @transaction.atomic
    def create(self, request):
        """
        영화 리뷰 생성
        - POST /reviews/
        """
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        review = ReviewService().create(user=request.user, **serializer.validated_data)
        rtn = ReviewSerializer(review).data

        return Response(rtn, status=status.HTTP_201_CREATED)

    @transaction.atomic
    def update(self, request, pk):
        """
        영화 리뷰 수정
        - PUT /reviews/{review_id}/
        """
        try:
            review = Review.objects.get(id=pk)
        except Review.DoesNotExist:
            return Response({"error": "Does not Exists."}, status=status.HTTP_404_NOT_FOUND)
        if review.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        review = ReviewService().update(review, request.data)
        rtn = ReviewSerializer(review).data
        return Response(rtn, status=status.HTTP_200_OK)

    @transaction.atomic
    def destroy(self, request, pk):
        """
        영화 리뷰 삭제
        - DELETE /reviews/{review_id}/
        """
        try:
            review = Review.objects.get(id=pk)
        except Review.DoesNotExist:
            return Response({"error": "Does not Exists."}, status=status.HTTP_404_NOT_FOUND)
        if review.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        ReviewService().delete(review)
        return Response(status=status.HTTP_200_OK)

from django.db import transaction
from django.db.models import Avg
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from review.models import Review
from review.serializers import ReviewSerializer


class ReviewViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk):
        """
        영화 리뷰 디테일 조회
        - GET /review/{review_id}/
        """
        try:
            review = Review.objects.get(id=pk)
        except Review.DoesNotExist:
            return Response({"error": "Does not Exists."}, status=status.HTTP_404_NOT_FOUND)
        return Response(ReviewSerializer(review).data, status=status.HTTP_200_OK)

    @transaction.atomic
    def create(self, request):
        """
        영화 리뷰 생성
        - POST /reviews/
        """
        # todo: 없는 movie_id 처리
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review = Review.objects.create(user=request.user, **serializer.validated_data)
        movie = review.movie
        updated_rating = Review.objects.filter(movie=movie) \
            .aggregate(rating=Avg('rating'))['rating']

        movie.rating = updated_rating
        movie.save()
        return Response(ReviewSerializer(review).data, status=status.HTTP_201_CREATED)

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
        text = request.data.get('text')
        if text is not None:
            review.text = text
        rating = request.data.get('rating')
        if rating is not None:
            review.rating = rating
            movie = review.movie
            updated_rating = Review.objects.filter(movie=movie) \
                .aggregate(rating=Avg('rating'))['rating']

            movie.rating = updated_rating
            movie.save()
        review.save()
        return Response(ReviewSerializer(review).data, status=status.HTTP_200_OK)

    @transaction.atomic
    def destroy(self, request, pk):
        """
        영화 리뷰 삭제
        - DELETE /reviews/{review_id}/
        """
        # todo: 리뷰 삭제시 영화 평점 업데이트
        try:
            review = Review.objects.get(id=pk)
        except Review.DoesNotExist:
            return Response({"error": "Does not Exists."}, status=status.HTTP_404_NOT_FOUND)
        if review.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        movie = review.movie
        updated_rating = Review.objects.filter(movie=movie) \
            .aggregate(rating=Avg('rating'))['rating']

        movie.rating = updated_rating
        movie.save()
        review.delete()
        return Response(status=status.HTTP_200_OK)

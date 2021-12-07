from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from vote.models import ReviewVote
from vote.serializers import ReviewVoteSerializer


class ReviewVoteViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def create(self, request):
        """
        영화 리뷰 추천 생성
        - POST /review_votes/
        """
        # todo: 없는 review_id 처리
        serializer = ReviewVoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review_vote = ReviewVote.objects.create(user=request.user, **serializer.validated_data)
        review = review_vote.review
        review.count_vote += 1
        review.save()
        return Response(ReviewVoteSerializer(review_vote).data, status=status.HTTP_201_CREATED)

    @transaction.atomic
    def destroy(self, request, pk):
        """
        영화 리뷰 삭제
        - DELETE /review_votes/{review_vote_id}/
        """
        try:
            review_vote = ReviewVote.objects.get(id=pk)
        except ReviewVote.DoesNotExist:
            return Response({"error": "Does not Exists."}, status=status.HTTP_404_NOT_FOUND)
        if review_vote.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        review = review_vote.review
        review.count_vote -= 1
        review.save()
        review_vote.delete()
        return Response(status=status.HTTP_200_OK)

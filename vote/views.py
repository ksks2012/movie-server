from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class ReviewVoteViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        """
        영화 리뷰 생성
        - POST /review_votes/
        """
        pass

    def delete(self, request, pk):
        """
        영화 리뷰 삭제
        - DELETE /review_votes/{review_vote_id}/
        """
        pass

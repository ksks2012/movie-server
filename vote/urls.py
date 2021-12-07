from django.urls import path, include
from rest_framework.routers import SimpleRouter

from vote.views import ReviewVoteViewSet

app_name = 'vote'

router = SimpleRouter()

router.register('review_votes', ReviewVoteViewSet, basename='review_votes')

urlpatterns = [
    path('', include((router.urls)))
]

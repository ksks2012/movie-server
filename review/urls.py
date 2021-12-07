from django.urls import path, include
from rest_framework.routers import SimpleRouter

from review.views import ReviewViewSet

app_name = 'review'

router = SimpleRouter()

router.register('reviews', ReviewViewSet, basename='reviews')

urlpatterns = [
    path('', include((router.urls)))
]

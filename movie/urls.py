from django.urls import path, include
from rest_framework.routers import SimpleRouter

from movie.views import MovieViewSet

app_name = 'movie'

router = SimpleRouter()

router.register('movies', MovieViewSet, basename='movies')

urlpatterns = [
    path('', include((router.urls)))
]

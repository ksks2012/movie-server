from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

from movie.serializers import MovieDetailSerializer


class MovieAutoSchema:
    retrieve_schema = dict(
        name="GET /movies/{movie_id}/",
        decorator=extend_schema(
            responses={
                200: MovieDetailSerializer,
                404: {"error": dict(error="Does not Exists.")}
            }
        )
    )

    list_schema = dict(
        name="rrr",
        decorator=extend_schema(
            parameters=[
                OpenApiParameter(
                    name='title',
                    type=OpenApiTypes.STR,
                    location=OpenApiParameter.QUERY,
                    description='Search by title'
                ),
                OpenApiParameter(
                    name='year',
                    type=OpenApiTypes.INT,
                    location=OpenApiParameter.QUERY,
                    description='Search by year'
                ),
                OpenApiParameter(
                    name='genres',
                    type=OpenApiTypes.STR,
                    location=OpenApiParameter.QUERY,
                    description='Search by genres'
                ),
                OpenApiParameter(
                    name='ordering',
                    type=OpenApiTypes.STR,
                    location=OpenApiParameter.QUERY,
                    description='order by rating',
                    examples=[
                        OpenApiExample(
                            'Descending',
                            value='-rating'
                        ),
                        OpenApiExample(
                            'Ascending',
                            value='rating'
                        )
                    ]
                ),
            ]
        )
    )

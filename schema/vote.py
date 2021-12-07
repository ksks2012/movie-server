from drf_spectacular.utils import extend_schema


class ReviewVoteAutoSchema:
    destroy_schema = dict(
        name="DELETE /review_votes/{review_vote_id}/",
        decorator=extend_schema(
            responses={
                200: None,
            }
        )
    )

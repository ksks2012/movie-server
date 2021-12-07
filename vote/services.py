from vote.models import ReviewVote


class ReviewVoteService:
    def create(self, user, **validated_data):
        review_vote = ReviewVote.objects.create(user=user, **validated_data)
        review = review_vote.review
        review.count_vote += 1
        review.save()
        return review_vote

    def delete(self, review_vote):
        review = review_vote.review
        review.count_vote -= 1
        review.save()
        review_vote.delete()

from sm_2 import SM2Scheduler, Card, ReviewLog
import json
import pytest
from copy import deepcopy

class TestSM2:

    def test_serialize(self):

        scheduler = SM2Scheduler()

        card = Card()
        old_card = deepcopy(card)

        # card is json-serializable
        assert type(json.dumps(card.to_dict())) == str

        # card can be serialized and de-serialized while remaining the same
        card_dict = card.to_dict()
        copied_card = Card.from_dict(card_dict)
        assert vars(card) == vars(copied_card)
        assert card.to_dict() == copied_card.to_dict()

        # review the card and perform more tests
        rating = 5
        card, review_log = scheduler.review_card(card, rating)

        review_log_dict = review_log.to_dict()
        copied_review_log = ReviewLog.from_dict(review_log_dict)
        assert review_log.to_dict() == copied_review_log.to_dict()
        # can use the review log to recreate the card that was reviewed
        assert old_card.to_dict() == Card.from_dict(review_log.to_dict()['card']).to_dict()

        # the new reviewed card can be serialized and de-serialized while remaining the same
        card_dict = card.to_dict()
        copied_card = Card.from_dict(card_dict)
        assert vars(card) == vars(copied_card)
        assert card.to_dict() == copied_card.to_dict()

    # TODO: add tests for interval lengths
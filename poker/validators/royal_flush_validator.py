from poker.validators import StraightFlushValidator


class RoyalFlushValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = 'Royal Flush'

    def is_valid(self):
        straight_flush_validator = StraightFlushValidator(cards=self.cards)
        if straight_flush_validator.is_valid():
            straight_flush_validator = straight_flush_validator.valid_cards()
            is_royal = straight_flush_validator[-1].rank == 'Ace'
            return is_royal

        return False

    def valid_cards(self):
        return StraightFlushValidator(cards=self.cards).valid_cards()

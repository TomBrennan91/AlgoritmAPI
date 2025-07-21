from poker.card import Card
from poker.hand_type import HandType


class Hand:
    """
    Represents a poker hand and provides functionalities to evaluate its type and characteristics.

    This class models a hand of poker cards and determines its classification according to poker
    rules. It provides methods to check specific hand properties such as whether the hand forms
    a flush or a straight and calculates the poker hand type by analyzing the ranks and suits of
    individual cards.

    :ivar hand_str: The string representation of the hand.
    :type hand_str: str
    :ivar cards: A list of Card objects representing the cards in the hand.
    :type cards: list[Card]
    :ivar rank_count: A Counter object tracking the occurrence of each rank in the hand.
    :type rank_count: Counter
    :ivar ranks_descending_importance: A list of ranks sorted by their significance (frequency and value).
    :type ranks_descending_importance: list[int]
    :ivar hand_type: The type of poker hand as determined by poker rules (e.g., flush, straight).
    :type hand_type: HandType
    :ivar flush: Indicates whether the hand is a flush.
    :type flush: bool
    :ivar straight: Indicates whether the hand is a straight.
    :type straight: bool
    """
    hand_str: str
    cards: list[Card]
    rank_count: Counter
    ranks_descending_importance: list[int]
    hand_type: int
    flush: bool
    straight: bool

    def __repr__(self):
        return f"Hand(hand_str={self.hand_str!r}, hand_type={self.hand_type.name}, cards={[str(card) for card in self.cards]})"

    def __init__(self, hand_str: str):
        self.hand_str = hand_str
        card_strs = hand_str.split(" ")
        self.cards = [Card(card_str) for card_str in card_strs]

        # sort hands by rank to make them easier to classify and compare
        self.cards.sort(key=lambda card: card.rank)

        self.flush = self.is_flush()
        self.straight = self.is_straight()
        self.rank_count = Counter([card.rank for card in self.cards])
        self.ranks_descending_importance = [rank for rank in
                                            sorted(self.rank_count, key=lambda k: (self.rank_count[k], k),
                                                   reverse=True)]
        self.hand_type = self.get_hand_type()

    def get_hand_type(self) -> int:
        """
        :return: an Enum representing the strongest poker category that the hand conforms to.
        """
        if self.flush and self.straight:
            return HandType.STRAIGHT_FLUSH

        sorted_count = sorted(self.rank_count.values(), reverse=True)

        if sorted_count[0] == 4:
            return HandType.FOUR

        if sorted_count[0] == 3 and sorted_count[1] == 2:
            return HandType.FULL_HOUSE

        if self.flush:
            return HandType.FLUSH

        if self.straight:
            return HandType.STRAIGHT

        if sorted_count[0] == 3:
            return HandType.THREE

        if sorted_count[0] == 2:
            if sorted_count[1] == 2:
                return HandType.TWO_PAIR
            return HandType.PAIR

        # if the Hand doesn't conform to any of the above hand types, it is simply a high card.
        return HandType.HIGH_CARD

    def is_flush(self) -> bool:
        """
        :return: True if the hand is a flush
        """
        suit = self.cards[0].suit
        for card in self.cards[1:]:
            if card.suit != suit:
                return False
        return True

    def is_straight(self) -> bool:
        """
        :return: True if the hand is straight
        """
        prev_rank = self.cards[0].rank
        for card in self.cards[1:]:
            if card.rank != prev_rank + 1:
                # we need to account for the possibility of an ace-low straight
                if card.rank == 14 and self.cards[0].rank == 2:
                    # mark the ace as low for determining high card later
                    card.rank = 1
                    return True
                return False
            prev_rank = card.rank
        return True

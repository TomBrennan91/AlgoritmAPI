class Card:
    """
    Represents a playing card with a rank and a suit.

    The Card class models a standard playing card, where each card has a rank
    (e.g., 2 through 10, Jack, Queen, King, Ace) and a suit (e.g., Hearts,
    Diamonds, Clubs, Spades). The rank is represented as an integer, with Ace
    being the highest rank (14) and cards like Jack, Queen, and King being
    represented by ranks 11, 12, and 13, respectively.

    :ivar rank: The rank of the card, represented as an integer. The rank can
        range from 2 to 14, where 14 represents an Ace, 13 a King, 12 a Queen,
        and 11 a Jack.
    :type rank: int
    :ivar suit: The suit of the card, represented as a single character string
        (e.g., 'H' for Hearts, 'D' for Diamonds, 'C' for Clubs, 'S' for Spades).
    :type suit: str
    """
    rank: int = 0
    suit: str = 'X'

    def __repr__(self):
        return f"Card(rank={self.rank}, suit={self.suit!r})"

    def __init__(self, card_str: str):
        if len(card_str) < 2 or len(card_str) > 3:
            raise ValueError("Card string must be exactly two or three characters long")

        self.suit = card_str[len(card_str) - 1]

        if len(card_str) == 3 and card_str[0] == '1' and card_str[1] == '0':
            self.rank = 10
        else:
            rank_chr = card_str[0]

            if rank_chr.isdigit():
                self.rank = int(card_str[0])
            elif rank_chr == 'A':
                self.rank = 14
            elif rank_chr == 'K':
                self.rank = 13
            elif rank_chr == 'Q':
                self.rank = 12
            elif rank_chr == 'J':
                self.rank = 11

class Card:
    rank : int = 0
    suit : str = 'X'

    def __init__(self, card_str: str):
        if len(card_str) < 2:
            raise ValueError("Card must be at least 2 characters")

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




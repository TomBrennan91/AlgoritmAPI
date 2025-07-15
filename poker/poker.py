from collections import Counter
from poker.card import Card
from enum import Enum

class HandType(Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR = 8
    STRAIGHT_FLUSH = 9

def best_hand(hands_str: list[str]) -> list[str]:
    """
    :param hands_str: a list of strings each representing a set of five playing cards
    :return: The winning poker hand from the given hands
    """
    hands = {}
    best_hand_type = HandType.HIGH_CARD.value
    for hand_str in hands_str:
        card_strs = hand_str.split(" ")
        hand = []
        for card_str in card_strs:
            hand.append(Card(card_str))
        hand = list(map(Card, card_strs))
        hand.sort(key=lambda card: card.rank)
        hand_type = get_hand_type(hand)
        if int(hand_type.value) > best_hand_type:
            best_hand_type = hand_type

        hands[hand_str] = [hand_type, hand]

    best_hands = {k: v for k, v in hands.items() if v[0].value == best_hand_type}

    highest_ranked_best_hands = []
    for high_card_idx in range (4, -1, -1):
        # if there are multiple each of the highest value type, return the one with the highest rank.

        highest_card = 0
        highest_ranked_best_hands = []
        for hand_str, hand in best_hands.items():
            if hand[1][high_card_idx].rank > highest_card:
                highest_card = hand[1][high_card_idx].rank
                highest_ranked_best_hands = [hand_str]
            elif hand[1][high_card_idx].rank == highest_card:
                highest_ranked_best_hands.append(hand_str)

        best_hands = {k: v for k, v in best_hands.items() if k in highest_ranked_best_hands}

        if len(highest_ranked_best_hands) == 1:
            return highest_ranked_best_hands

    return highest_ranked_best_hands


def get_hand_type(hand) -> HandType:
    if is_flush(hand) and is_straight(hand):
        return HandType.STRAIGHT_FLUSH

    ranks = []
    for card in hand:
        ranks.append(card.rank)
    rank_count = Counter(ranks)

    if rank_count[0] == 4:
        return HandType.FOUR

    if rank_count[0] == 3 and rank_count[1] == 2:
        return HandType.FULL_HOUSE

    if is_flush(hand):
        return HandType.FLUSH

    if is_straight(hand):
        return HandType.STRAIGHT

    if rank_count[0] == 3:
        return HandType.THREE

    if rank_count[0] == 2:
        if rank_count[1] == 2:
            return HandType.TWO_PAIR
        return HandType.PAIR

    return HandType.HIGH_CARD

def is_flush(hand : list[Card]) -> bool:
    suit = hand[0].suit
    for card in hand[1:]:
        if card.suit != suit:
            return False
    return True

def is_straight(hand : list[Card]) -> bool:
    prev_rank = hand[0].rank
    for card in hand[1:]:
        if card.rank != prev_rank + 1:
            # There's a chance that th
            if card.rank == 14 and hand[0].rank == 2 and prev_rank == 13:
                return True
            return False
        prev_rank = card.rank
    return True

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

def best_hand(hands_str: list[str]) -> str:
    """
    :param hands_str: a list of strings each representing a set of five playing cards
    :return: The winning poker hand from the given hands
    """
    hands = {}
    for hand_str in hands_str:
        card_strs = hand_str.split(" ")
        hand = list(map(Card, card_strs))
        hand.sort(key=lambda card: card.rank)
        hand_type = get_hand_type(hand)
        hands[hand] = hand_type



    best_hand_type = max(hands.values())
    best_hands = [k for k, v in hands.items() if v == best_hand_type]

    if len(best_hands) == 1:
        return best_hands[0]


    # if there are multiple each of the highest value type, return the one with the highest rank.
    highest_card = 0
    highest_ranked_best_hand = None
    for joint_best_hand in best_hands:
        if joint_best_hand[4].rank > highest_card:
            highest_card = joint_best_hand[4].rank
            highest_ranked_best_hand = joint_best_hand

    return highest_ranked_best_hand


def get_hand_type(hand) -> HandType:
    if is_flush(hand) and is_straight(hand):
        return HandType.STRAIGHT_FLUSH

    ranks = list(map(Card.rank, hand))
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

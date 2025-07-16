import pprint
from collections import Counter
from enum import Enum

from poker.card import Card

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
        hand = [Card(card_str) for card_str in card_strs]

        # sort hands by rank to make them easier to classify and compare
        hand.sort(key=lambda card: card.rank)

        hand_type = get_hand_type(hand).value
        if hand_type > best_hand_type:
            best_hand_type = hand_type

        # store all this information in a dict to make it easier to keep track of.
        hands[hand_str] = [hand_type, hand]

    # # eliminate all the elements in the dict where the hand type isn't as strong as the best hand type
    # best_hands = {k: v for k, v in hands.items() if v[0].value == best_hand_type}


    pprint.pprint(hands)
    best_hands = {}

    print(best_hand_type)

    for hand_str, hand_info in hands.items():
        pprint.pprint(best_hand_type)
        pprint.pprint(hand_info[0])
        if hand_info[0] == best_hand_type:
            best_hands[hand_str] = hand_info
    pprint.pprint(best_hands)

    highest_ranked_best_hands = []
    for high_card_idx in range (4, -1, -1):
        # if there are multiple each of the highest value type, return the one with the highest ranked cards.

        highest_card = 0
        highest_ranked_best_hands = []
        for hand_str, hand in best_hands.items():
            if hand[1][high_card_idx].rank > highest_card:
                highest_card = hand[1][high_card_idx].rank
                highest_ranked_best_hands = [hand_str]
            elif hand[1][high_card_idx].rank == highest_card:
                highest_ranked_best_hands.append(hand_str)

        best_hands = {k: v for k, v in best_hands.items() if k in highest_ranked_best_hands}

        # if we have a single winning hand, return it, otherwise continue to compare the next highest ranked card.
        if len(highest_ranked_best_hands) == 1:
            return highest_ranked_best_hands

    # if we have reached here, we have multiple hands of the same type and identical rankings of cards.
    return highest_ranked_best_hands


def get_hand_type(hand) -> HandType:
    """
    :param hand: the hand that we want to determine the hand_type
    :return: an Enum representing the strongest poker category that the hand conforms to.
    """
    if is_flush(hand) and is_straight(hand):
        return HandType.STRAIGHT_FLUSH

    ranks = []
    for card in hand:
        ranks.append(card.rank)

    rank_count = sorted(Counter(ranks).values(), reverse=True)

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

    # if the Hand doesn't conform to any of the above hand types, it is simply a high card.
    return HandType.HIGH_CARD

def is_flush(hand : list[Card]) -> bool:
    """
    :param hand: list of Cards
    :return: True if the hand is a flush
    """
    suit = hand[0].suit
    for card in hand[1:]:
        if card.suit != suit:
            return False
    return True

def is_straight(hand : list[Card]) -> bool:
    """
    :param hand: list of Cards in ascending order of rank (aces high)
    :return: True if the hand is a straight
    """
    prev_rank = hand[0].rank
    for card in hand[1:]:
        if card.rank != prev_rank + 1:
            # There's a chance that th
            if card.rank == 14 and hand[0].rank == 2 and prev_rank == 13:
                return True
            return False
        prev_rank = card.rank
    return True

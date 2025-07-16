import pprint

from poker.hand import Hand


def best_hand(hands_str: list[str]) -> list[str]:
    """
    :param hands_str: a list of strings each representing a set of five playing cards
    :return: The winning poker hand from the given hands
    """
    hands = []

    for hand_str in hands_str:
        hands.append(Hand(hand_str))

    best_hand_type = max(hand.hand_type.value for hand in hands)

    best_hands = []
    # eliminate all the elements in the dict where the hand type isn't as strong as the best hand type
    for hand in hands:
        if hand.hand_type.value == best_hand_type:
            best_hands.append(hand)
    pprint.pprint(best_hands)

    return determine_tie_winner(best_hands)

def determine_tie_winner(best_hands : list[Hand]) -> list[str]:

    for high_card_idx in range (4, -1, -1):
        # if there are multiple each of the highest value type, return the one with the highest ranked cards.

        highest_card = 0
        highest_ranked_best_hands = []
        for hand in best_hands:
            if hand.cards[high_card_idx].rank > highest_card:
                highest_card = hand.cards[high_card_idx].rank
                highest_ranked_best_hands = [hand]
            elif hand.cards[high_card_idx].rank == highest_card:
                highest_ranked_best_hands.append(hand)

        best_hands = highest_ranked_best_hands

        # if we have a single winning hand, return it, otherwise continue to compare the next highest ranked card.
        if len(highest_ranked_best_hands) == 1:
            return [best_hands[0].hand_str]

    # if we have reached here, we have multiple hands of the same type and identical rankings of cards.
    return [hand.hand_str for hand in best_hands]


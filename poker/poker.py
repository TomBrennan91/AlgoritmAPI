from poker.hand import Hand

def best_hand(hands_str: list[str]) -> list[str]:
    """
    :param hands_str: a list of strings each representing a set of five playing cards
    :return: The winning poker hand from the given hands
    """
    hands = [Hand(hand_str) for hand_str in hands_str]

    # eliminate all the elements in the dict where the hand type isn't as strong as the best hand type
    best_hand_type = max(hand.hand_type.value for hand in hands)
    best_hands = [hand for hand in hands if hand.hand_type.value == best_hand_type]

    if len(best_hands) == 1:
        return [best_hands[0].hand_str]
    else:
        return determine_tie_winner(best_hands)

def determine_tie_winner(best_hands : list[Hand]) -> list[str]:

    for i in range(len(best_hands[0].ranks_descending_importance)):
        # if there are multiple each of the highest value type, return the one with the highest ranked cards.

        highest_card = 0
        highest_ranked_best_hands = []
        for hand in best_hands:
            if hand.ranks_descending_importance[i] > highest_card:
                highest_card = hand.ranks_descending_importance[i]
                highest_ranked_best_hands = [hand]
            elif hand.ranks_descending_importance[i] == highest_card:
                highest_ranked_best_hands.append(hand)

        best_hands = highest_ranked_best_hands

        # if we have a single winning hand, return it, otherwise continue to compare the next highest ranked card.
        if len(highest_ranked_best_hands) == 1:
            return [best_hands[0].hand_str]

    # if we have reached here, we have multiple hands of the same type and identical rankings of cards.
    return [hand.hand_str for hand in best_hands]


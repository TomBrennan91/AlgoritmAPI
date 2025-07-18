from poker.hand import Hand


def best_hand(hands_str: list[str]) -> list[str]:
    """
    Determine the strongest hand(s) from a list of poker hand strings.

    The function analyzes a list of poker hands represented as strings, calculates
    the type of each hand, and identifies the ones with the strongest hand type. If
    there is a single best hand, the function returns it. If there is a tie between
    hands with the strongest type, it determines the winner among them.

    :param hands_str: A list of poker hand strings where each string represents a player's hand.
    :return: A list containing the strongest hand string(s). If there is a single winner, the list
             will have one element. In the case of a tie, multiple hand strings may be returned.
    """
    hands = [Hand(hand_str) for hand_str in hands_str]

    # eliminate all the elements in the dict where the hand type isn't as strong as the best hand type
    best_hand_type = max(hand.hand_type.value for hand in hands)
    best_hands = [hand for hand in hands if hand.hand_type.value == best_hand_type]

    if len(best_hands) == 1:
        return [best_hands[0].hand_str]
    else:
        return determine_tie_winner(best_hands)


def determine_tie_winner(best_hands: list[Hand]) -> list[str]:
    """
    Determines the winner(s) among a list of Hands that have achieved the same hand type.
    In case of a tie, it compares ranks in descending importance to find the hand(s) with
    the highest individual card ranks. If ranks cannot break the tie, all tied hands
    are returned.

    :param best_hands: A list of Hand objects where each represents a player's best poker
        hand. All hands in the input list have achieved the same poker hand type and are
        considered potential winners.
    :return: A list of strings representing the hand descriptions of the winning Hand
        object(s). If there is a tie that cannot be resolved by comparing ranks,
        multiple hand descriptions are returned.
    """

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

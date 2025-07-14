import unittest
from poker.poker import best_hand

class TestPoker(unittest.TestCase):

    def test_single_hand_always_wins(self):
        self.assertEqual(best_hand(["4S 5S 7H 8D JC"]), ["4S 5S 7H 8D JC"])


    def test_highest_card_out_of_all_hands_wins(self):
        self.assertEqual(
            best_hand(["4D 5S 6S 8D 3C", "2S 4C 7S 9H 10H", "3S 4S 5D 6H JH"]),
            ["3S 4S 5D 6H JH"],
        )


    def test_a_tie_has_multiple_winners(self):
        self.assertEqual(
            best_hand(
                [
                    "4D 5S 6S 8D 3C",
                    "2S 4C 7S 9H 10H",
                    "3S 4S 5D 6H JH",
                    "3H 4H 5C 6C JD",
                ]
            ),
            ["3S 4S 5D 6H JH", "3H 4H 5C 6C JD"],
        )


    def test_multiple_hands_with_the_same_high_cards_tie_compares_next_highest_ranked_down_to_last_card(
            self,
    ):
        self.assertEqual(
            best_hand(["3S 5H 6S 8D 7H", "2S 5D 6D 8C 7S"]), ["3S 5H 6S 8D 7H"]
        )


    def test_winning_high_card_hand_also_has_the_lowest_card(self):
        self.assertEqual(
            best_hand(["2S 5H 6S 8D 7H", "3S 4D 6D 8C 7S"]), ["2S 5H 6S 8D 7H"]
        )

# Final Project
# Fall 2025, CS 5001
# Chenhao (Alex) Hou
# 11/16/2025

import unittest, actionControl
from cardAndType import Card, HandType

class Test_userAction(unittest.TestCase):

    def test_rank_suit_to_card(self):
        expected_rank = "A"
        expected_suit = "Spade"

        test_rank = actionControl.rank_suit_to_card("A", "S").rank
        test_suit = actionControl.rank_suit_to_card("A", "S").suit

        self.assertEqual(test_rank, expected_rank)
        self.assertEqual(test_suit, expected_suit)

    def test_update_user_cards(self):
        expected_rank = "K"
        expected_suit1 = "Club"
        expected_suit2 = "Heart"

        test_rank = actionControl.update_user_cards([Card(0), Card(13)], Card(27), 0)[1].rank
        test_suit1 = actionControl.update_user_cards([Card(0), Card(13)], Card(27), 0)[1].suit
        test_suit2 = actionControl.update_user_cards([Card(0), Card(13)], Card(27), 0)[0].suit

        self.assertEqual(test_rank, expected_rank)
        self.assertEqual(test_suit1, expected_suit1)
        self.assertEqual(test_suit2, expected_suit2)
    
    def test_is_user_winner(self):
        expected_user_type = "Full House"
        expected_computer_type = "Flush"
        expected_bool = False

        computer_cards = [Card(0), Card(9)]
        board_cards = [Card(5), Card(6), Card(7), Card(18), Card(37)]
        user_cards1 = [Card(44), Card(20)]
        user_cards2 = [Card(29), Card(43)]

        test_user_type = actionControl.is_user_winner(computer_cards, board_cards, user_cards1)[0]
        test_computer_type = actionControl.is_user_winner(computer_cards, board_cards, user_cards1)[1]
        test_bool = actionControl.is_user_winner(computer_cards, board_cards, user_cards2)

        self.assertEqual(test_user_type, expected_user_type)
        self.assertEqual(test_computer_type, expected_computer_type)
        self.assertEqual(test_bool, expected_bool)


if __name__ == "__main__":
    unittest.main()

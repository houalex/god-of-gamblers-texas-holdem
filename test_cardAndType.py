# Final Project
# Fall 2025, CS 5001
# Chenhao (Alex) Hou
# 11/14/2025

import unittest
from cardAndType import Card

class TestCard(unittest.TestCase):

    def test_suit(self):
        expected_suit1 = "Spade"
        expected_suit2 = "Heart"

        test_Card1 = Card(12)
        test_Card2 = Card(13)

        self.assertEqual(test_Card1.suit, expected_suit1)
        self.assertEqual(test_Card2.suit, expected_suit2)
    
    def test_rank(self):
        expected_rank1 = "2"
        expected_rank2 = "A"

        test_card1 = Card(25)
        test_card2 = Card(26)

        self.assertEqual(test_card1.rank, expected_rank1)
        self.assertEqual(test_card2.rank, expected_rank2)


if __name__ == "__main__":
    unittest.main()

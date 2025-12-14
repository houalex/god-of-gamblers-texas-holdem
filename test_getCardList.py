# Final Project
# Fall 2025, CS 5001
# Chenhao (Alex) Hou
# 11/15/2025

import unittest, getCardList
from cardAndType import Card

class Test_getCardList(unittest.TestCase):

    def test_get_original_list(self):
        expected_length = 11
        expected_type = True
        
        test_length = len(getCardList.get_original_list())
        test_type = isinstance(getCardList.get_original_list()[5], Card)

        self.assertEqual(test_length, expected_length)
        self.assertEqual(test_type, expected_type)
    
    def test_build_card_database(self):
        original_list = getCardList.get_original_list()
        expected_length = 462
        expeted_type = True

        test_length = len(getCardList.build_card_database(original_list))
        test_type = isinstance(getCardList.build_card_database(original_list)[0][0][4], Card)

        self.assertEqual(test_length, expected_length)
        self.assertEqual(test_type, expeted_type)

    def test_count_same(self):
        cardList1 = [Card(0), Card(1), Card(2), Card(3), Card(4)]
        cardList2 = [Card(2), Card(3), Card(5), Card(6), Card(7)]
        expeted_count = 2

        test_count = getCardList.count_same(cardList1, cardList2)

        self.assertEqual(test_count, expeted_count)

    def test_minus_list(self):
        cardList1 = [Card(0), Card(1), Card(2), Card(3), Card(4)]
        cardList2 = [Card(2), Card(3), Card(5), Card(6), Card(7)]
        expected_list = [Card(0), Card(1), Card(4)]
        expected_length = 3
        expeted_last_number = 4

        test_list = getCardList.minus_list(cardList1, cardList2)
        test_length = len(test_list)
        test_last_number = test_list[2].number

        self.assertEqual(test_length, expected_length)
        self.assertEqual(test_last_number, expeted_last_number)

    def test_select_cards(self):
        expected_length_all = 4
        expected_length1 = 5
        expected_length2 = 2
        expected_type = True
        expected_overlap = 0

        test_output = getCardList.select_cards()
        test_length_all = len(test_output)
        test_length1 = len(test_output[0])
        test_length2 = len(test_output[3])
        test_type = isinstance(test_output[1][1], Card)
        test_overlap = getCardList.count_same(test_output[1], test_output[2])

if __name__ == "__main__":
    unittest.main()

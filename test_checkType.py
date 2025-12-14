# Final Project
# Fall 2025, CS 5001
# Chenhao (Alex) Hou
# 11/14/2025

import unittest, checkType
from cardAndType import Card

class Test_checkType(unittest.TestCase):

    """
    Tests of checkType.check_flush()
    """
    def test_check_flush_good_cards(self):
        good_cardList = [Card(39), Card(42), Card(44), Card(45), Card(48)]
        expected_good_cards = True

        test_good_cards = checkType.check_flush(good_cardList)

        self.assertEqual(test_good_cards, expected_good_cards)

    def test_check_flush_bad_cards(self):
        bad_cardList = [Card(3), Card(12), Card(29), Card(44), Card(48)]
        expected_bad_cards = False

        test_bad_cards = checkType.check_flush(bad_cardList)

        self.assertEqual(test_bad_cards, expected_bad_cards)

    """
    Tests of checkType.check_straight()
    """
    def test_check_straight_good_cards(self):
        good_cardList1 = [Card(0), Card(22), Card(23), Card(37), Card(12)] #A2345
        good_cardList2 = [Card(26), Card(40), Card(2), Card(16), Card(17)] #AKQJT
        good_cardList3 = [Card(47), Card(48), Card(49), Card(50), Card(51)] #65432

        expected_check_straight1 = True
        expected_check_straight2 = True
        expected_check_straight3 = True

        test_check_straight1 = checkType.check_straight(good_cardList1)
        test_check_straight2 = checkType.check_straight(good_cardList2)
        test_check_straight3 = checkType.check_straight(good_cardList3)

        self.assertEqual(test_check_straight1, expected_check_straight1)
        self.assertEqual(test_check_straight2, expected_check_straight2)
        self.assertEqual(test_check_straight3, expected_check_straight3)
    
    def test_check_straight_bad_cards(self):
        bad_cardList1 = [Card(0), Card(9), Card(10), Card(11), Card(11)]
        bad_cardList2 = [Card(25), Card(26), Card(27), Card(28), Card(29)]

        expected_check_straight1 = False
        expected_check_straight2 = False

        test_check_straight1 = checkType.check_straight(bad_cardList1)
        test_check_straight2 = checkType.check_straight(bad_cardList2)

        self.assertEqual(test_check_straight1, expected_check_straight1)
        self.assertEqual(test_check_straight2, expected_check_straight2)

    """
    Tests of checkType.check_same_ranks()
    """
    def test_check_same_4(self): #test Four of a Kind
        cardList = [Card(0), Card(13), Card(26), Card(39), Card(5)]
        expected_length = 4
        expected_rank = "A"
        expected_bool = True

        test_list = checkType.check_same_ranks(cardList)
        test_length = len(test_list[4])
        test_rank = test_list[4][0].rank
        test_bool = test_list[0]

        self.assertEqual(test_length, expected_length)
        self.assertEqual(test_rank, expected_rank)
        self.assertEqual(test_bool, expected_bool)

    def test_check_same_32(self): #test Full House
        cardList = [Card(14), Card(27), Card(40), Card(9), Card(22)]
        expected_length1 = 3
        expected_rank1 = "K"
        expected_length2 = 2
        expected_rank2 = "5"

        test_list = checkType.check_same_ranks(cardList)
        test_length1 = len(test_list[3])
        test_rank1 = test_list[3][0].rank
        test_length2 = len(test_list[2])
        test_rank2 = test_list[2][0].rank

        self.assertEqual(test_length1, expected_length1)
        self.assertEqual(test_rank1, expected_rank1)
        self.assertEqual(test_length2, expected_length2)
        self.assertEqual(test_rank2, expected_rank2)
        
    """
    Tests of checkType.check_type()
    """
    def test_royal_flush(self):
        cardList = [Card(0), Card(1), Card(2), Card(3), Card(4)]
        expected_handType = 0
        
        test_handType = checkType.check_type(cardList)[0].number

        self.assertEqual(test_handType, expected_handType)

    def test_straight_flush(self):
        cardList = [Card(0), Card(9), Card(10), Card(11), Card(12)]
        expected_handType = 1
        expected_remainder= 9

        test_list = checkType.check_type(cardList)
        test_handType = test_list[0].number
        test_remainder = test_list[1]

        self.assertEqual(test_handType, expected_handType)
        self.assertEqual(test_remainder, expected_remainder)

    def test_FourOfAKind(self):
        cardList = [Card(3), Card(16), Card(29), Card(42), Card(7)]
        expected_handType = 2
        expected_remainder1 = 3
        expected_remainder2 = 7

        test_list = checkType.check_type(cardList)
        test_handType = test_list[0].number
        test_remainder1 = test_list[1]
        test_remainder2 = test_list[2]

        self.assertEqual(test_handType, expected_handType)
        self.assertEqual(test_remainder1, expected_remainder1)
        self.assertEqual(test_remainder2, expected_remainder2)

    def test_FullHouse(self):
        cardList = [Card(4), Card(17), Card(30), Card(35), Card(48)]
        expected_handType = 3
        expected_remainder1 = 4
        expected_remainder2 = 9

        test_list = checkType.check_type(cardList)
        test_handType = test_list[0].number
        test_remainder1 = test_list[1]
        test_remainder2 = test_list[2]

        self.assertEqual(test_handType, expected_handType)
        self.assertEqual(test_remainder1, expected_remainder1)
        self.assertEqual(test_remainder2, expected_remainder2)

    def test_Flush(self):
        cardList = [Card(0), Card(2), Card(4), Card(6), Card(8)]
        expected_handType = 4
        expected_remainder1 = 0
        expected_remainder2 = 8

        test_list = checkType.check_type(cardList)
        test_handType = test_list[0].number
        test_remainder1 = test_list[1]
        test_remainder2 = test_list[5]

        self.assertEqual(test_handType, expected_handType)
        self.assertEqual(test_remainder1, expected_remainder1)
        self.assertEqual(test_remainder2, expected_remainder2)

    def test_Straight(self):
        cardList1 = [Card(39), Card(22), Card(10), Card(50), Card(12)]
        cardList2 = [Card(39), Card(27), Card(2), Card(42), Card(4)]
        expected_handType1 = 5
        expected_remainder1 = 9
        expected_handType2 = 5
        expected_remainder2 = 0

        test_list1 = checkType.check_type(cardList1)
        test_list2 = checkType.check_type(cardList2)
        test_handType1 = test_list1[0].number
        test_remainder1 = test_list1[1]
        test_handType2 = test_list2[0].number
        test_remainder2 = test_list2[1]
    
    def test_ThreeOfAKind(self):
        cardList = [Card(3), Card(17), Card(10), Card(36), Card(49)]
        expected_handType = 6
        expected_remainder1 = 10
        expected_remainder2 = 4

        test_list = checkType.check_type(cardList)
        test_handType = test_list[0].number
        test_remainder1 = test_list[1]
        test_remainder2 = test_list[3]
    
    def test_TwoPairs(self):
        cardList = [Card(13), Card(39), Card(7), Card(12), Card(38)]
        expected_handType = 7
        expected_remainder1 = 0
        expected_remainder2 = 12

        test_list = checkType.check_type(cardList)
        test_handType = test_list[0].number
        test_remainder1 = test_list[1]
        test_remainder2 = test_list[2]

        self.assertEqual(test_handType, expected_handType)
        self.assertEqual(test_remainder1, expected_remainder1)
        self.assertEqual(test_remainder2, expected_remainder2)

    def test_OnePair(self):
        cardList = [Card(39), Card(2), Card(15), Card(30), Card(11)]
        expected_handType = 8
        expected_remainder1 = 2
        expected_remainder2 = 11

        test_list = checkType.check_type(cardList)
        test_handType = test_list[0].number
        test_remainder1 = test_list[1]
        test_remainder2 = test_list[4]

        self.assertEqual(test_handType, expected_handType)
        self.assertEqual(test_remainder1, expected_remainder1)
        self.assertEqual(test_remainder2, expected_remainder2)

    def test_HighCard(self):
        cardList = [Card(2), Card(16), Card(30), Card(10), Card(50)]
        expected_handType = 9
        expected_remainder1 = 2
        expected_remainder2 = 11

        test_list = checkType.check_type(cardList)
        test_handType = test_list[0].number
        test_remainder1 = test_list[1]
        test_remainder2 = test_list[5]

        self.assertEqual(test_handType, expected_handType)
        self.assertEqual(test_remainder1, expected_remainder1)
        self.assertEqual(test_remainder2, expected_remainder2)


if __name__ == "__main__":
    unittest.main()

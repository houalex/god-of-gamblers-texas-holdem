# Final Project
# Fall 2025, CS 5001
# Chenhao (Alex) Hou
# 11/14/2025

from cardAndType import Card, HandType

def check_flush(cardList):
    """
    Param cardList: a list of 5 cards sorted by remainder
    Verify whether they have same suit and return T/F
    """
    if len(cardList) != 5:
        raise ValueError("cardList should have 5 cards")
    for i in range(4):
        if not isinstance(cardList[i], Card):
            raise TypeError("elements of cardList need to be cards")
        if cardList[i].suit != cardList[i + 1].suit:
            return False
    return True

def check_straight(cardList):
    """
    Param cardList: a list of 5 cards sorted by remainder
    Verify whether they are straight and return T/F
    A2345 is considered straight
    """
    if len(cardList) != 5:
        raise ValueError("cardList should have 5 cards")
    for i in range(1, 4):
        if not isinstance(cardList[i], Card):
            raise TypeError("elements of cardList need to be cards")
        if not cardList[i].remainder + 1 == cardList[i + 1].remainder:
            return False
    if cardList[0].remainder == 0 and cardList[1].remainder == 9:
        return True
    elif cardList[0].remainder + 1 == cardList[1].remainder:
        return True
    else:
        return False

def check_same_ranks(cardList):
    """
    Param cardList: a list of 5 cards sorted by remainder
    Return a list of lists of cards, in which:
        list[4] includes cards that can make Four of a Kind
        list[3] includes cards that can make Three of a Kind
        list[2] includes cards that can make Pairs
        list[0] True if same ranks are found else False
    """
    all_remainders = [[] for _ in range(13)]
    same_ranks = [[] for _ in range(5)]
    same_ranks[0] = False
    if len(cardList) != 5:
        raise ValueError("cardList should have 5 cards")
    for card in cardList:
        if not isinstance(card, Card):
            raise TypeError("elements of cardList need to be cards")
        index = card.remainder
        all_remainders[index].append(card)
    for cardlist in all_remainders:
        if len(cardlist) == 4:
            for card in cardlist:
                same_ranks[4].append(card)
            same_ranks[0] = True
        elif len(cardlist) == 3:
            for card in cardlist:
                same_ranks[3].append(card)
            same_ranks[0] = True
        elif len(cardlist) == 2:
            for card in cardlist:
                same_ranks[2].append(card)
            same_ranks[0] = True
    return same_ranks

def check_type(cardList):
    """
    Param cardList: a list of 5 cards sorted by remainder
    Return: a list of HandType followed by remainders(used to compare similar hands)
            list length is 6. if not enough remainders, fill it with 0
        Ex. check_type([Card(0), Card(13), Card(1), Card(27), Card(51)]) should return
            [HandType(7), 0, 1, 12, 0, 0]
            HandType(7).name is Two Pairs, 0 represents a pair of "A", 1 represents a pair of "K", 12 represents a kicker of "2"
    """
    output = [0 for _ in range(6)]
    isFlush = check_flush(cardList)
    isStraight = check_straight(cardList)
    if isFlush and isStraight:
        if cardList[0].remainder == 0 and cardList[1].remainder == 1:
            output[0] = HandType(0)
        else:
            output[0] = HandType(1)
            if cardList[0].remainder == 0:
                output[1] = 9
            else:
                output[1] = cardList[0].remainder
    else:
        sameRankList = check_same_ranks(cardList)
        if sameRankList[4] != []:
            output[0] = HandType(2)
            first_remainder = sameRankList[4][0].remainder
            output[1] = first_remainder
            for i in range(5):
                if cardList[i].remainder != first_remainder:
                    output[2] = cardList[i].remainder
        elif sameRankList[3] != [] and sameRankList[2] != []:
            output[0] = HandType(3)
            output[1] = sameRankList[3][0].remainder
            output[2] = sameRankList[2][0].remainder
        elif isFlush:
            output[0] = HandType(4)
            for i in range(5):
                output[i + 1] = cardList[i].remainder
        elif isStraight:
            output[0] = HandType(5)
            if cardList[0].remainder == 0 and cardList[1].remainder == 9:
                output[1] = 9
            else:
                output[1] = cardList[0].remainder
        elif sameRankList[3] != []:
            output[0] = HandType(6)
            output[1] = sameRankList[3][0].remainder
            j = 2
            for i in range(5):
                if cardList[i].remainder != output[1]:
                    output[j] = cardList[i].remainder
                    j += 1
        elif len(sameRankList[2]) == 4:
            output[0] = HandType(7)
            output[1] = sameRankList[2][0].remainder
            output[2] = sameRankList[2][2].remainder
            for i in range(5):
                if not cardList[i].remainder in output[1:]:
                    output[3] = cardList[i].remainder
        elif len(sameRankList[2]) == 2:
            output[0] = HandType(8)
            output[1] = sameRankList[2][0].remainder
            j = 2
            for i in range(5):
                if cardList[i].remainder != output[1]:
                    output[j] = cardList[i].remainder
                    j += 1
        else:
            output[0] = HandType(9)
            for i in range(5):
                output[i + 1] = cardList[i].remainder
    return output

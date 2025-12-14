# Final Project
# Fall 2025, CS 5001
# Chenhao (Alex) Hou
# 11/15/2025

import random
from cardAndType import Card
from checkType import check_type

def get_original_list():
    """
    Shuffle list[0, 1, 2, ..., 51]
    Turn first 11 numbers to cards and return list of cards
    """
    deck = [i for i in range(52)]
    random.shuffle(deck)
    card_list = []
    for i in range(11):
        card = Card(deck[i])
        card_list.append(card)
    card_list.sort(key=lambda x: x.remainder)
    return card_list

def build_card_database(original_list):
    """
    Param: original list of 11 cards
    get all combination of C(5, 11)
    create a database where element is a list of [combination, hand_ranking, hand_type]
    sort the database by hand_ranking, databse[0][0] is the best 5 of 11 cards
    """
    card_database = []
    for i in range(len(original_list) - 4):
        for j in range(i + 1, len(original_list) - 3):
            for k in range(j + 1, len(original_list) - 2):
                for l in range(k + 1, len(original_list) - 1):
                    for m in range(l + 1, len(original_list)):
                        cardList = [original_list[i], original_list[j], original_list[k], original_list[l], original_list[m]]
                        type_result = check_type(cardList)
                        hand_ranking = type_result[0].number * 10000000000 + type_result[1] * 100000000 + type_result[2] * 1000000 + type_result[3] * 10000 + type_result[4] * 100 + type_result[5]
                        hand_type = type_result[0]
                        element = [cardList, hand_ranking, hand_type]
                        card_database.append(element)
    card_database.sort(key=lambda x: x[1])
    return card_database

def count_same(cardList1, cardList2):
    """
    Return count of same eleements of two card lists
    count_same([Card(0), Card(1), Card(2)], [Card(0), Card(3)]) = 1
    """
    numberset1 = set()
    numberset2 = set()
    for i in range(len(cardList1)):
        numberset1.add(cardList1[i].number)
    for i in range(len(cardList2)):
        numberset2.add(cardList2[i].number)
    return len(numberset1 & numberset2)

def minus_list(cardList1, cardList2):
    """
    Return a list of cards that are in cardList1 but not in cardList2
    minus_list([Card(0), Card(1), Card(2)], [Card(1), Card(3)]) = [Card(0), Card(2)]
    """
    numberlist1 = []
    numberset2 = set()
    output = []
    for i in range(len(cardList1)):
        numberlist1.append(cardList1[i].number)
    for i in range(len(cardList2)):
        numberset2.add(cardList2[i].number)
    for i in range(len(cardList1)):
        if not numberlist1[i] in numberset2:
            output.append(Card(numberlist1[i]))
    return output

def select_cards():
    """
    from 11 cards, 5 cards in best hand are top cards
    method to select board cards and pocket cards:
        reserved cards - list[1] and list[3] top cards
        computer cards - list[0] and list[1] of highest ranking hand(name: current_board_cards) that includes no reserved cards and includes at least one of other top cards
        board cards - highest ranking hand that includes no reserved cards, no customer cards but includes all cards of current_board_cards.
    Return [
        list of board cards,
        list of computer cards,
        list of user cards,
        list of reserved cards
        ]
    """
    original_list = get_original_list()
    card_database = build_card_database(original_list)
    top_card_list = card_database[0][0] #best hand in card_database

    reserved_cards = [top_card_list[1], top_card_list[3]] #reserved_cards makes sure user can win
    isComputerCards = False
    index = 1 
    while isComputerCards == False and index < len(card_database) - 1:
        current_card_list = card_database[index][0]
        """
        find highest ranking list from card_database that has no resereved cards and at least one top card.
        this list main include 1 or 2 or 3 of the 3 top cards(exclude 2 reserved cards), take out list[0] and list[1] as computer pocket cards.
        put the 3 top cards back to the list (name current_board_cards)
        if its lenghth is smaller than 5, continue finding the highest ranking list from card_databse that includes all elements of current_board_cards.
        then this list is board_cards
        """
        if count_same(current_card_list, reserved_cards) == 0 and count_same(current_card_list, top_card_list) >= 1:
            isComputerCards = True
            computer_options = minus_list(current_card_list, top_card_list)
            computer_cards = computer_options[:2]
        else:
            index += 1
    current_board_cards = computer_options[2:] + [top_card_list[0], top_card_list[2], top_card_list[4]]
    current_board_cards.sort(key=lambda x: x.remainder)
    if len(current_board_cards) == 5:
        board_cards = current_board_cards
    else:
        isBoardCards = False
        index += 1
        while isBoardCards == False and index < len(card_database) - 1:
            current_card_list = card_database[index][0]
            if count_same(current_card_list, reserved_cards) == 0 and count_same(current_card_list, computer_cards) == 0 and count_same(current_card_list, current_board_cards) == len(current_board_cards):
                board_cards = current_card_list
                isBoardCards = True
            else:
                index += 1
    user_cards = minus_list(minus_list(minus_list(original_list, board_cards), computer_cards), reserved_cards)
    return [board_cards, computer_cards, user_cards, reserved_cards]

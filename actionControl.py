# Final Project
# Fall 2025, CS 5001
# Chenhao (Alex) Hou
# 11/16/2025

from cardAndType import Card, HandType
from printingCards import printing_cards
from getCardList import select_cards, count_same, build_card_database

def rank_suit_to_card(rank: str, suit: str):
    """
    Param rank, suit are strings, suit needs to be in ("S", "H", "C", "D")
    Return a card based on rank and suit.
        Ex. rank_suit_to_card("A", "S") return Card(0)
    """
    if rank == "A":
        remainder = 0
    elif rank == "K":
        remainder = 1
    elif rank == "Q":
        remainder = 2
    elif rank == "J":
        remainder = 3
    else:
        remainder = 14 - int(rank)
    if suit == "S":
        coefficient = 0
    elif suit == "H":
        coefficient = 1
    elif suit == "C":
        coefficient = 2
    elif suit == "D":
        coefficient = 3
    number = coefficient * 13 + remainder
    return Card(number)

def replace_first_card(rank_limit):
    """
    User replace one card with any card of a specified rank.
    Return [new card, 0/1], where 0 means to replace left card and 1 means to replace right card.
    """
    print(f'You can replace one of your cards with a card of "{rank_limit}".')
    left_or_right = input("Which card do you want to change? L/R\n").upper()
    while left_or_right != "L" and left_or_right != "R":
        print('Input must be "L" or "R".')
        left_or_right = input("Which card do you want to change? L/R\n").upper()
    if left_or_right == "L":
        left_or_right = 0
    else:
        left_or_right = 1
    new_suit = input("Choose a suit: S/H/C/D\n").upper()
    while not new_suit in ("S", "H", "C", "D"):
        print('Input must be "S" or "H" or "C" or "D".')
        new_suit = input("Choose a suit: S/H/C/D\n").upper()
    new_card = rank_suit_to_card(rank_limit, new_suit)
    return [new_card, left_or_right]

def replace_second_card(suit_limit):
    """
    User replace one card with any card of a specified rank.
    Return the new card
    """
    print(f'You can replace the other card with a card of "{suit_limit}".')
    new_rank = input("Choose a rank: A/K/Q/J/10/9/8/7/6/5/4/3/2\n").upper()
    while not new_rank in ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"):
        print('Input must be "A" or "K" or "Q" or "J" or "10" or "9" or "8" or "7" or "6" or "5" or "4" or "3" or "2".')
        new_rank = input("Choose a rank: A/K/Q/J/10/9/8/7/6/5/4/3/2\n").upper()
    new_suit = suit_limit[0]
    new_card = rank_suit_to_card(new_rank, new_suit)
    return [new_card]

def print_three_cardLists(computer_cards, board_cards, user_cards):
    """
    This function defines the format of printing three cardLists.
    """
    print("Computer pocket cards: ")
    print(printing_cards(computer_cards))
    print("Board cards: ")
    print(printing_cards(board_cards))
    print("Your pocket cards: ")
    print(printing_cards(user_cards))

def update_user_cards(user_cards, new_card, index):
    """
    update user_cards after user decides replace to which card
    """
    new_user_cards = []
    new_user_cards.append(new_card)
    new_user_cards.append(user_cards[1-index])
    new_user_cards.sort(key=lambda x: x.remainder)
    return new_user_cards

def is_user_winner(computer_cards, board_cards, user_cards):
    """
    Param: list of 2 pocket cards of computer, list of 5 board cards, list of 2 pocket cards of user
    Return [user hand type, computer hand type] if user wons else Flase.
    """
    computer_whole = computer_cards + board_cards
    computer_whole.sort(key = lambda x: x.remainder)
    user_whole = user_cards + board_cards
    user_whole.sort(key = lambda x: x.remainder)

    computer_best_hand = build_card_database(computer_whole)[0]
    user_best_hand = build_card_database(user_whole)[0]

    if user_best_hand[1] < computer_best_hand[1]:
        return [user_best_hand[2].name, computer_best_hand[2].name]
    else:
        return False

def one_round():
    """
    1. computer's two pocket cards, five board cards, user's two pocket cards are printed
    2. user can replace one if his cards with a card of a sepcified rank
    3. if user is still behind, user can replace the other pocket card with a card of a specified suit
    4. print whether the user wins
    """
    selected_cards = select_cards() #get cardLists
    board_cards = selected_cards[0]
    computer_cards = selected_cards[1]
    user_cards = selected_cards[2]
    reseved_cards = selected_cards[3]
    rank_limit = reseved_cards[0].rank
    suit_limit = reseved_cards[1].suit
    forbid_cards = board_cards + computer_cards + user_cards

    replace_count = 0
    lose_count = 0

    print_three_cardLists(computer_cards, board_cards, user_cards)

    isFirstOK = False
    while not isFirstOK:
        first_replace_output = replace_first_card(rank_limit)
        if count_same([first_replace_output[0]], forbid_cards) != 0: #validate dupilication
            print("You cannot choose a card same to existing cards.")
        else:
            isFirstOK = True
            forbid_cards.append(first_replace_output[0])
            replace_count += 1
    
    new_user_cards = update_user_cards(user_cards, first_replace_output[0], first_replace_output[1])

    print_three_cardLists(computer_cards, board_cards, new_user_cards)

    user_computer_type = is_user_winner(computer_cards, board_cards, new_user_cards)
    if user_computer_type == False:
        isSecondOK = False
        while not isSecondOK:
            second_replace_output = replace_second_card(suit_limit)
            if count_same([second_replace_output[0]], forbid_cards) != 0:
                print("You cannot choose a card same to existing cards.")
            else:
                isSecondOK = True
                replace_count += 1
        
        new_user_cards = [first_replace_output[0], second_replace_output[0]]
        new_user_cards.sort(key=lambda x: x.remainder)

        print_three_cardLists(computer_cards, board_cards, new_user_cards)

        user_computer_type = is_user_winner(computer_cards, board_cards, new_user_cards)
        if user_computer_type == False:
            print("You lose.")
            lose_count += 1
        else:
            user_type_name = user_computer_type[0]
            computer_type_name = user_computer_type[1]
            print(f'Congratulations! You win! {user_type_name} over {computer_type_name}!')
    else:
        user_type_name = user_computer_type[0]
        computer_type_name = user_computer_type[1]
        print(f'Congratulations! You win! {user_type_name} over {computer_type_name}!')

    return [replace_count, lose_count]

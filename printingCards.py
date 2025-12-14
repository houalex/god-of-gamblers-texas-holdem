# Final Project
# Fall 2025, CS 5001
# Chenhao (Alex) Hou
# 11/15/2025

from cardAndType import Card

def printing_suit(card):
    """
    extend suit to length of 9 with " " and "|"
    """
    printing_suit = card.suit
    if card.suit == "Heart" or card.suit == "Spade":
        printing_suit = " " + card.suit + " "
    elif card.suit == "Club":
        printing_suit = " " + card.suit + "  "
    return "|" + printing_suit + "|"

def printing_rank(card):
    """
    extend rank to length of 9 with " " and "|"
    """
    if card.rank == "10":
        printing_rank = " 10    "
    else:
        printing_rank = " " + card.rank + "     "
    return "|" + printing_rank + "|"

def printing_cards(cardList):
    """
    Param cardList is a list of cards
    Return a string ready to print
    """
    count = len(cardList)
    suit_line = ""
    rank_line = ""
    for i in range(count):
        suit_line += printing_suit(cardList[i])
        rank_line += printing_rank(cardList[i])
    vertical_line = "+-------+" * count + "\n"
    empty_line = "|       |" * count + "\n"
    return vertical_line + rank_line + "\n" + empty_line * 2 + suit_line + "\n" + vertical_line

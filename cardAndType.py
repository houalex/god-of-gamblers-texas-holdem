# Final Project
# Fall 2025, CS 5001
# Chenhao (Alex) Hou
# 11/14/2025

class Card:

    def __init__(self, number: int):
        """
        0, 1, 2, ..., 12: A Spade, K Spade, Q Spade, ..., 2 Spade
        13, 14, 15, ..., 25: A Heart, K Heart, Q Heart, ..., 2 Heart
        26, 27, 28, ..., 38: A Club, K Club, Q Club, ..., 2 Club
        39, 40, 41, ..., 51: A Diamond, K Diamond, Q Diamond, ..., 2 Diamond
        """
        if not 0 <= int(number) <= 51:
            raise ValueError("Card number is between 0 and 51")
        self.number = number
        suitList = ["Spade", "Heart", "Club", "Diamond"]
        self.suit = suitList[number // 13]
        self.remainder = number % 13
        if self.remainder == 0:
            self.rank = "A"
        elif self.remainder == 1:
            self.rank = "K"
        elif self.remainder == 2:
            self.rank = "Q"
        elif self.remainder == 3:
            self.rank = "J"
        else:
            self.rank = str(14 - self.remainder)
    
    def __str__(self):
        return f'{self.rank} {self.suit}'

class HandType:
    def __init__(self, number: int):
        number_to_name = {
            0: "Royal Flush",
            1: "Straight Flush",
            2: "Four of a Kind",
            3: "Full House",
            4: "Flush",
            5: "Straight",
            6: "Three of a Kind",
            7: "Two Pairs",
            8: "One Pair",
            9: "High Card"
        }
        self.number = number
        self.name = number_to_name[number]

    def __str__(self):
        return f'{self.number}: {self.name}'

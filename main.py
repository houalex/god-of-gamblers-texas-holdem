# Final Project
# Fall 2025, CS 5001
# Chenhao (Alex) Hou
# 11/17/2025

from cardAndType import Card
from actionControl import one_round

def main():
    print("\n\nYou will play 10 rounds of Texas Hold'em with computer.\nIn each round, you are allowed to replace one of your pocket cards, and then the other if needed, to improve your hand and beat the computer.\nYour goal is to minimize your replacement.\n")
    round_count = 1
    replace_count = 0
    lose_count = 0
    while round_count < 11:
        print(f'\nRound {round_count}: \n')
        li = one_round()
        replace_count += li[0]
        lose_count += li[1]
        round_count += 1
    total_score = 600 - 10 * replace_count - 40 * lose_count #maximun score is 500(needs luck)
    print(f'Game over.\nYour total score is {total_score}/500.')


if __name__ == "__main__":
    main()

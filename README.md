# God of Gamblers: Texas Hold'em Card Replacement Simulator

This is my final project for my first coding course.

The program simulates old Hong Kong gambling movies, like *God of Gamblers*, where the main characters have a "superpower" to secretly replace their pocket cards in a Texas Hold'em game.

The user plays against the computer for **10 rounds**.  
In each round, the user is initially behind, but is allowed to "cheat" in a restricted way to improve their hand and try to beat the computer with as **few replacements as possible**.

---

## Game Rules & Mechanics

### Basic Setup

- Game type: **Texas Hold'em** (heads-up: user vs computer)
- Each round has:
  - 2 pocket cards for the computer
  - 2 pocket cards for the user
  - 5 board (community) cards

The program makes sure cards are selected completely randomly and user can beat computer if right replacements are made.

---

### Special "Superpower" – Two-Step Replacement

In each round, the user has up to **two chances** to replace their pocket cards:

#### First replacement – fixed **rank**

- The program gives you a **rank limit** (for example `"8"`).
- You may:
  - Choose **which pocket card** to replace: `L` (left) or `R` (right)
  - Choose **any suit**: `S` (spade), `H` (heart), `C` (club), `D` (diamond)
- The new card will have:
  - The given **rank**
  - The **suit** you choose
- You cannot choose a card already exists on the table.

#### Second replacement – fixed **suit**

If you are still behind after the first replacement:

- The program gives you a **suit limit** (for example `"H"`).
- Now you replace the **other pocket card**:
  - The suit is fixed to the given suit (e.g. hearts).
  - You may choose **any rank**: `A/K/Q/J/10/9/8/7/6/5/4/3/2`.
- Again, you cannot choose a card that already exists on the table.

After each replacement, the program compares:

- your best 5-card hand  
- vs. the computer's best 5-card hand  

and decides who wins the round.

---

### Example Scenario

Computer’s pocket cards:  
- K of hearts  
- Q of clubs  

Board cards:  
- A of spades  
- J of hearts  
- 10 of hearts  
- 7 of spades  
- 7 of hearts  

Your pocket cards:  
- Q of hearts  
- 7 of clubs  

You are behind.  
Suppose your **rank limit** is `"8"`.

You can replace **one** of your pocket cards with an 8 of any suit:

- **Best move**:  
  Replace **7 of clubs** with **8 of hearts** → you now have a **flush** in hearts.

- **Worse move**:  
  Replace **Q of hearts**, and then hope to get A/J/10 on the second replacement for a **full house**.  
  This depends more on luck and is usually not as good as the guaranteed flush.

The goal of the game is to learn to **evaluate hands** and **choose better replacements** with minimal cheating.

---

### Scoring

Over 10 rounds, the program tracks:

- `replace_count`: how many times you replaced a card  
- `lose_count`: how many rounds you lost  

At the end:

total_score = 600 - 10 * replace_count - 40 * lose_count
print(f"Your total score is {total_score}/500.")

---

## Requirements

- Python 3.x
- No external libraries needed

---

## How to Run

1. Clone repository
2. Enter folder
3. Run:
    ```bash
    python main.py
    ```

---

## Future Improvements

- Add an AI opponent that plays real Texas Hold'em strategy
  I am currently learning introductory artificial intelligence techniques to enable the user to play against a true strategic computer opponent, rather than a fixed hand-comparison system.
  The first upgrade will be a simple perceptron model that allows the computer to make basic decisions such as fold, call, or raise based on hand strength and board texture.

- Upgrade to a Q-learning agent
  After the perceptron stage, the next goal is to implement a reinforcement learning model using Q-learning.
  The AI will learn optimal strategies by simulating large numbers of hands, adjusting its policy through reward signals, and gradually improving its long-term expected value in each decision state.
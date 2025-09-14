
# 🐍 Conditional Probability in Python
# Problem 1: Dice 🎲
# Find 𝑃(Even∣>3)
# P(Even∣>3).
import random

# Simulation
N = 100000
outcomes = [random.randint(1,6) for _ in range(N)]

# Condition B: >3
B = [x for x in outcomes if x > 3]

# A ∩ B: even and >3
AB = [x for x in B if x % 2 == 0]

P_A_given_B = len(AB)/len(B)
print("P(Even | >3) =", P_A_given_B)


# ✅ Output ~ 0.666 (≈ 2/3).

# Problem 2: Cards ♠️

# Find 
# 𝑃(Ace∣Spade)
# P(Ace∣Spade).

import itertools

# Deck of cards
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck = list(itertools.product(ranks, suits))

# Condition B: spade
B = [card for card in deck if card[1] == "Spades"]

# A ∩ B: Ace of Spades
AB = [card for card in B if card[0] == "A"]

P_A_given_B = len(AB)/len(B)
print("P(Ace | Spade) =", P_A_given_B)


✅ Output = 1/13 ≈ 0.0769.

# Problem 3: Students 👨‍🎓

# 25 boys, 15 girls. 10 boys passed, 5 girls passed.
# Find 
# 𝑃(Boy∣Passed)
# P(Boy∣Passed).

# Data
boys = 25
girls = 15
boys_pass = 10
girls_pass = 5

# Condition B: Passed
total_pass = boys_pass + girls_pass

# A ∩ B: Boys who passed
AB = boys_pass

P_A_given_B = AB / total_pass
=======
# 🐍 Conditional Probability in Python
# Problem 1: Dice 🎲
# Find 𝑃(Even∣>3)
# P(Even∣>3).
import random

# Simulation
N = 100000
outcomes = [random.randint(1,6) for _ in range(N)]

# Condition B: >3
B = [x for x in outcomes if x > 3]

# A ∩ B: even and >3
AB = [x for x in B if x % 2 == 0]

P_A_given_B = len(AB)/len(B)
print("P(Even | >3) =", P_A_given_B)


# ✅ Output ~ 0.666 (≈ 2/3).

# Problem 2: Cards ♠️

# Find 
# 𝑃(Ace∣Spade)
# P(Ace∣Spade).

import itertools

# Deck of cards
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck = list(itertools.product(ranks, suits))

# Condition B: spade
B = [card for card in deck if card[1] == "Spades"]

# A ∩ B: Ace of Spades
AB = [card for card in B if card[0] == "A"]

P_A_given_B = len(AB)/len(B)
print("P(Ace | Spade) =", P_A_given_B)


✅ Output = 1/13 ≈ 0.0769.

# Problem 3: Students 👨‍🎓

# 25 boys, 15 girls. 10 boys passed, 5 girls passed.
# Find 
# 𝑃(Boy∣Passed)
# P(Boy∣Passed).

# Data
boys = 25
girls = 15
boys_pass = 10
girls_pass = 5

# Condition B: Passed
total_pass = boys_pass + girls_pass

# A ∩ B: Boys who passed
AB = boys_pass

P_A_given_B = AB / total_pass
print("P(Boy | Passed) =", P_A_given_B)

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


# ✅ Output = 1/13 ≈ 0.0769.

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

# Output = 1/13 ≈ 0.0769.

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



#************Expectation Example************************
# Dice Example
import random

trails = 1000
result  = [random.randint(1,6) for _ in range(trails)]

expectation = sum(result) / trails

print("Dice ka theoretical expectation = 3.5")
print("Dice ka simulation expectation =", expectation)

# Coin toss ezample
import random

trails = 100000
result = [random.randint(0, 1) for _ in range(trails)]

expectation = sum(result) / trails
print("Coin ka theoretical expectation = 0.5")
print("Coin ka simulation expectation =", expectation)



#********************Variance + Expectation**************************
import random 
trails = 1000
result = [random.randint(1, 6) for _ in range(trails)]

expectation = sum(result) / trails

variance = sum((x - expectation) ** 2 for x in result) / trails
# 🔎 Breakdown:
# for x in results
# → Matlab hum har ek outcome (dice ka result ya coin ka result) ko le rahe hain.
# Example: agar dice 5 bar roll hua aur results [2, 6, 4, 3, 5] aaye to x pehle 2 lega, phir 6, phir 4 ... aise sab par chalega.
# (x - expectation)
# → Har result ka difference nikal rahe hain uske average (expectation) se.
# Example: Dice ka expectation = 3.5
# Agar x = 2 → (2 - 3.5) = -1.5
# Agar x = 6 → (6 - 3.5) = 2.5
# (x - expectation) ** 2
# → Difference ka square kar rahe hain (taake minus signs khatam ho jayein aur distance positive ho jaye).
# (-1.5)² = 2.25
# (2.5)² = 6.25
# 👉 Yeh step "spread" ko highlight karta hai.
# sum(... for x in results)
# → Ab sab squared differences ko add kar rahe hain.
# Example: 2.25 + 6.25 + 0.25 + ... (jitne results hain).
# / trials
# → Total results (trials) ki tadaad se divide kar dete hain, taake average mil jaye.
# Matlab yeh “mean squared difference” hai → isko hi variance kehte hain.

print("Coin ka theoretical expectation = 0.5")
print("Coin ka simulation expectation =", expectation)
print("Coin ka simulation variance =", variance)
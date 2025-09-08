#*****************Chi-square Test using NumPy*****************
# 📝 Practice Problem – Candies Distribution
# Problem Statement:
# Ek bag me 120 candies hain, 4 colors me:
# Color	Observed Count
# Red	40
# Blue	30
# Green	25
# Yellow	25
# Tum check karo candies uniform distribution follow kar rahi hain ya nahi.
# Steps follow karna:
# Expected frequency nikalna (Total ÷ Number of categories)
# Chi-Square Statistic calculate karna
# P-value find karna
# Decide karna: Null hypothesis reject karni hai ya nahi (threshold = 0.05)
import numpy as np
from scipy.stats import chi2
observed = np.array([40, 30, 25, 25])
expected = np.array([30, 30, 30, 30])  # Since uniform distribution is expected
chi_square_statistic = ((observed - expected) ** 2 / expected).sum()
p_value = 1 - chi2.cdf(chi_square_statistic, df=len(observed)-1)
print("Chi-Square Statistic:", chi_square_statistic)
print("P-value:", p_value)
if p_value < 0.05:
    print("Null hypothesis rejected: Candies do not follow uniform distribution.")
else:
    print("Null hypothesis accepted: Candies follow uniform distribution.")
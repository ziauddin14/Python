import numpy as np
from scipy import stats

# ---------------- t-Test Example ----------------
# Do chhote groups ke marks
# group1 = [85, 90, 78, 88, 95]  # Boys
# group2 = [80, 85, 82, 87, 90]  # Girls

# # Two-Sample t-Test (equal variance assume karte hain)
# t_stat, p_value = stats.ttest_ind(group1, group2)
# print("=== t-Test ===")
# print("t-Statistic:", t_stat)
# print("p-Value:", p_value)
# if p_value < 0.05:
#     print("Result: Reject Null Hypothesis → Groups are significantly different")
# else:
#     print("Result: Fail to Reject Null Hypothesis → No significant difference")

# ---------------- z-Test Example ----------------
# z-Test me population SD pata hona chahiye
# pop_mean = 80          # Population mean
# pop_std = 10           # Population standard deviation
# sample = [85, 90, 78, 88, 95]
# n = len(sample)

# z formula: z = (sample_mean - pop_mean) / (pop_std / sqrt(n))
# sample_mean = np.mean(sample)
# z = (sample_mean - pop_mean) / (pop_std / np.sqrt(n))

# Two-tailed p-value from z
# p = 2 * (1 - stats.norm.cdf(abs(z)))

# print("\n=== z-Test ===")
# print("Sample Mean:", sample_mean)
# print("z-Statistic:", z)
# print("p-Value:", p)
# if p < 0.05:
#     print("Result: Reject Null Hypothesis → Sample mean is significantly different from population mean")
# else:
#     print("Result: Fail to Reject Null Hypothesis → No significant difference")
    
# Note: z-Test tab use karte hain jab population SD pata ho aur sample size bada ho (n > 30)
# t-Test tab use karte hain jab population SD pata na ho aur sample size chhota ho (n < 30)
# (yahan humne chhote sample ke liye t-Test aur z-Test dono dikhaye hain for demonstration)
# (real-world me aapko dono tests alag-alag situations me use karne chahiye)

#***********************📝 Practice Problem – t-Test & z-Test************************
# Scenario 1: t-Test
# Do groups ke students ke marks diye gaye hain:
# boys_marks = [78, 85, 88, 92, 80]
# girls_marks = [82, 79, 85, 87, 90]
# Tasks:
# Do groups ke average marks compare karne ke liye Two-Sample t-Test apply karo.
# p-Value calculate karo.
# Decide karo Null Hypothesis reject karni hai ya accept.
# boys_marks = [78, 85, 88, 92, 80]
# girls_marks = [82, 79, 85, 87, 90]
# t_stat, p_value = stats.ttest_ind(boys_marks,girls_marks)
# print("\n=== Practice Problem: t-Test ===")
# print("t-Statistic:", t_stat)
# print("p-Value:", p_value)
# if p_value < 0.05:
#     print("Result: Reject Null Hypothesis → Groups are significantly different")
# else:
#     print("Result: Fail to Reject Null Hypothesis → No significant difference")
    
# # Scenario 2: z-Test:
# Ek school ka population mean marks 75 hain aur population SD 8 hai.
# Sample students ke marks:
# sample_marks = [78, 82, 85, 80, 90]
# Tasks:
# Sample ka mean calculate karo.
# One-Sample z-Test apply karo.
# p-Value calculate karo.
# Decide karo Null Hypothesis reject karni hai ya accept.
sample_marks = [78, 82, 85, 80, 90]
pop_mean = 75
pop_std = 8
n = len(sample_marks)
sample_mean = np.mean(sample_marks)
z = (sample_mean - pop_mean) / (pop_std / np.sqrt(n))
p = 2 * (1 - stats.norm.cdf(abs(z)))
print("\n=== Practice Problem: z-Test ===")
print("Sample Mean:", sample_mean)
print("z-Statistic:", z)
print("p-Value:", p)
if p < 0.05:
    print("Result: Reject Null Hypothesis → Sample mean is significantly different from population mean")
else:
    print("Result: Fail to Reject Null Hypothesis → No significant difference")
    












# #Hints / Steps:
# t-Test ke liye scipy.stats.ttest_ind() use karo.
# z-Test ke liye formula:
# z = \frac{\text{sample_mean – population_mean}}{\text{population_SD / √n}}
# p-Value calculate karne ke liye 2*(1 - stats.norm.cdf(abs(z))).
# Significance level = 0.05


# Sort a list of numbers without using .sort() or sorted()
# [5,2,8,1] ==> [1,2,5,8]
nums = [5, 2, 8, 1]
n = len(nums)
for i in range(n):  # 0,1,2,3
    min_idx = i
    for j in range(i + 1, n):  # 1,2,3,
        if nums[j] < nums[min_idx]:
            min_idx = j
    nums[i], nums[min_idx] = nums[min_idx], nums[i]
print(nums)

# *********RLE (RUn-Lenght Encoding)'aaabbc' => 'a3b2c1' *************

text = "aaabbc"
encode = ""
count = 1
for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        encode += str(count) + text[i - 1]
        count = 1
encode += str(count) + text[-1]
print(encode)

# *****Decode*******

decode = ""
count = ""

for char in encode:
    if char.isdigit():
        count = char
    else:
        decode += char * int(count)
        count = ""
print(decode)
 
 
#Sliding window problem
#You are given a list of integers and number k find the maximum sum of any k consecutive elements
#Input : nums = [2,1,5,1,3,2], k =3  ====> output = 9
nums = [2,1,5,1,3,2]
k = int(input("Enter number of k: "))
window_slide = sum(nums[:k])
max_sum = window_slide
for i in range(k, len(nums)):
    window_sum += nums[i]
    window_sum -= nums[i - k]
    if window_sum > max_sum:
        max_sum = window_sum
print(max_sum)
 
sentence = "Artificial Intelligence"
# Count the Vowels
vowels = "aeiouAEIOU"
count = 0
for i in  sentence:
    if i in vowels:
      count += 1
print("Total Vowels:" , count)

vowels = "aeiouAEIOU"
count = 0
i = 0

while i < len(sentence):
    if sentence[i] in vowels:
        count += 1
    i += 1
print(count)

# ********************List in Python********************
fruits = ["apple", "mango", "banana"]
print(fruits[:2])
print(fruits.append("grapes"))
print(fruits.insert(1, "cherry"))
print(fruits.pop())
print(fruits.remove("mango"))
fruits[0] = "kiwi"
print(fruits)

numbers = [1,5,3,2,9,7,4]
print(len(numbers))
print(numbers.count(1))
print(max(numbers))
print(min(numbers))
print(numbers.reverse())
print(numbers.sort())
print(numbers.sort(reverse=True))


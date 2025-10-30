# ************Dict Comprehension in  Python*****************

squres = {x: x**2 for x in range(1, 6)}
print(squres)

# find the squres of even number
even_Squres = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_Squres)

# worrking with existing dictionary
temps_c = {"Karachi": 32, "Lahore": 35, "Quetta": 28}
temps_feh = {city: (temp * 9 / 5) + 32 for city, temp in temps_c.items()}
print(temps_feh)

students = {"Ali": 82, "Sara": 90, "Ahmed": 67, "Zara": 95}
passed_students = {
    name: ("you passed" if score > 70 else "You fail")
    for name, score in students.items()
}
print(passed_students)


# Dict comprehension on List
names = ["Ali", "Sara", "Ahmed", "Zara"]
name_value = {name: len(name) for name in names}
print(name_value)


# Dict Comprehension on word
word = "datascience"
char_frwq = {letter: word.count(letter) for letter in word}
print(char_frwq)

scores = {"A": 95, "B": 60, "C": 85}
resul_dicts = {k: v for k, v in scores.items() if v >= 80}
print(resul_dicts)


# ****************Generator Comprehension*****************
# Gen identify by () <== round brackets
gen = (x**2 for x in range(1, 6))
print(gen)


big_gen = (x**2 for x in range(10000000))
print(next(big_gen))
print(next(big_gen))
print(next(big_gen))
print(next(big_gen))
print(next(big_gen))


total = sum(x**2 for x in range(1000000))
print(total)

cube = (x**3 for x in range(1, 20) if x % 2 != 0)
for val in cube:
    print(val)  # end keyword is for spacing each other in one line


keys = ["name", "age", "city"]
values = ["Ali", 22, "Karachi"]
kyes = {keys[i]: values[i] for i in range(len(keys))}
print(kyes)


'''
{
    1:{1:1,2:2,3:3},
    2:{1:2,2:4,3:6},
    3:{1:3,2:6,3:9}
}
'''
output_dict = {
    i: {j: i * j for j in range(1, 4)} 
    for i in range(1, 4)
}
print(output_dict)


sentence = 'Artificial Intelligence changes everything'
len_sen = {word: len(word) for word in sentence.split()}
print(len_sen)


grades = {'Ali': 'A', 'Sara': 'B', 'Ahmed': 'A', "Zara": 'C'}
abc = {k : v for v,k in grades.items() }
print(abc)
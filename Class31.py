#*****************Python Practise*****************
s = input('Enter a number:')
product = 1
for i in s:
    product *= int(i)
print(product)

'''
Scenario
A bus pucksup and drops off passengers at each stop
You're given pairs: [got_on, got_off].
Your job: calculate how any people are on the bus at the end.
stops = [
    [3,0],
    [2,1],
    [4,2]
]
'''
stops = [
    [3, 0],
    [2, 1],
    [4, 2]
]

people = 0
for s in stops:
    people += s[0]
    people -= s[1]
print(people)

n = 12
xp = 0
for i in range(1, n+1):
    if i % 5 ==0:
        xp += 20
    else:
        xp += 10
print(xp)
        



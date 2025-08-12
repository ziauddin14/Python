# Write a program that:
# Prints even numbers from 1 to 20
# Skips numbers divisible by 3
for num in range(1,21):
    if num % 2 == 0:
        if num % 3 != 0:
            print(num)


# break and continue statement in Python's Loop
# break statement
for chocolate in ["dairy milk", "perk", "kit-kat", "5-star"]:
    if chocolate == "kit-kat":
        print("Yay! Kit-kat mil gayi ")
        break
    print("Yeh wali nahi chahiye:", chocolate)

# continue statement
for fruits in ["Apple", "Banana", "Mango","Orange"]:
    if fruits == "Banana":
        print("Banana nhi chahiye!")
        continue
    print("Hmm, ye fruit theek h!")
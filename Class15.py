

numbers = []
for i in range(5):
   num = int(input(f"Enter number {i+1}: "))
   if num < 0:
    print("Negative number entered! Stopping input early.")
    break
   numbers.append(num)
else:
    print("Analysis Complete ✅")
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
          even_numbers.append(n)
    odd_numbers = []
    for n in numbers:
        if n % 2 != 0:
            odd_numbers.append(n)
    total = 0
    for n in numbers:
        if n > 50:
            total += n
    print("\nEven numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)
    print("Total of numbers above 50:", total)


#Prime Numbers Using Loop:
print("Prime numbers between 2 and 50 are:")

for num in range(2, 51): 
    is_prime = True        
    for i in range(2, num):  
        if num % i == 0:     
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

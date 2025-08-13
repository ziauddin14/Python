def averag(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print("Average is:", sum / len(numbers))

# Example function call
averag(10, 20, 30)
# Function Arguments
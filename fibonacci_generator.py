# CodeAlpha Task 01 - Fibonacci Generator 


# Define a function to calculate Fibonacci numbers
def fibonacci(n):
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    else:
        # Recursive case: calculate Fibonacci number using recursion
        return fibonacci(n-1) + fibonacci(n-2)

# Take input from the user for the limit of Fibonacci series
num = int(input("Enter the limit: "))

# Loop through numbers up to the given limit
for i in range(num):
    # Print the Fibonacci number for each index in the series
    print(fibonacci(i), end=" ")


# JAIKUMAR R - 11/04/2024

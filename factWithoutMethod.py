'''

10) Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6

program:
# Input: Read the tuple values as a single line of space-separated integers
tuple_values = tuple(map(int, input().split()))

# Input: Read the value to count
x = int(input())

# Count the occurrences of x in the tuple
count_x = tuple_values.count(x)

# Function to calculate factorial without using factorial()
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Calculate the factorial of the count
factorial_value = calculate_factorial(count_x)

# Output: Print the count and the factorial value
print(factorial_value)
'''

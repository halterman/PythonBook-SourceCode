# Compute the greastest common factor of two integers
# provided by the user

# Prompt user for input
num1 = int(input('Please enter an integer: '))
num2 = int(input('Please enter another integer: '))

# Determine the smaller of num1 and num2
min = num1 if num1 < num2 else num2

# 1 definitely is a common factor to all ints
largest_factor = 1  
for i in range(1, min + 1):
    if num1 % i == 0 and num2 % i == 0:
        largest_factor = i   # Found larger factor
# Print the GCD
print(largest_factor)

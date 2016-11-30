#  Allow the user to enter a sequence of nonnegative
#  integers.  The user ends the list with a negative
#  integer.  At the end the sum of the nonnegative 
#  umbers entered is displayed.  The program prints 
#  zero if the user provides no nonnegative numbers.

entry = 0      # Ensure the loop is entered
sum = 0        # Initialize sum

#  Request input from the user
print("Enter numbers to sum, negative number ends list:")

while entry >= 0:          # A negative number exits the loop 
    entry = int(input())  # Get the value
    if entry >= 0:         # Is number nonnegative?
        sum += entry       # Only add it if it is nonnegative
print("Sum =", sum)        # Display the sum

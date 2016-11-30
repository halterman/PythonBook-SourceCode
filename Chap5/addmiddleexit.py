#  Allow the user to enter a sequence of nonnegative
#  numbers.  The user ends the list with a negative
#  number.  At the end the sum of the nonnegative 
#  numbers entered is displayed.  The program prints 
#  zero if the user provides no nonnegative numbers.

entry = 0      # Ensure the loop is entered
sum = 0        # Initialize sum

#  Request input from the user
print("Enter numbers to sum, negative number ends list:")

while True:                # Loop forever?  Not really
    entry = int(input())   # Get the value
    if entry < 0:          # Is number negative number?
        break              # If so, exit the loop
    sum += entry           # Add entry to running sum 
print("Sum =", sum)        # Display the sum

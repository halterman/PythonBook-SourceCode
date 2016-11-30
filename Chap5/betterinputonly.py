#  Require the user to enter an integer in the range 1-10
in_value = 0    # Ensure loop entry
attempts = 0    # Count the number of tries

#  Loop until the user supplies a valid number
while in_value < 1 or in_value > 10:
    in_value = int(input("Please enter an integer in the range 0-10: "))
    attempts += 1

#  Make singular or plural word as necessary
tries = "try" if attempts == 1 else "tries"
#  in_value at this point is guaranteed to be within range
print("It took you", attempts, tries, "to enter a valid number")

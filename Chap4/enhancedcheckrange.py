value = int(input("Please enter an integer value in the range 0...10: ")
if value >= 0:        # First check
    if value <= 10:   # Second check
        print(value, "is in range") 
    else:
        print(value, "is too large") 
else:
    print(value, "is too small") 
print("Done")

#  Add five nonnegative numbers supplied by the user
count = sum = 0
print('Please provide five nonnegative numbers when prompted')
while count < 5:
    # Get value from the user
    val = float(input('Enter number: '))
    if val < 0:
        print('Negative numbers not acceptable!  Terminating')
        break
    count += 1
    sum += val
else:
    print('Average =', sum/count) 

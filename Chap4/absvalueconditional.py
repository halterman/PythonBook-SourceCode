#  Acquire a number from the user and print its absolute value.  
n = int(input("Enter a number: "))
print('|', n, '| = ', (-n if n < 0 else n), sep='') 

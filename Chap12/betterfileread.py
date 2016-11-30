#  Sum the values in a text file containing integers
try:
    with open('mydata.dat') as f:
        sum = 0
        try:
            for line in f:
                sum += int(line)
        except Exception as er:
            print(er)  # Show the problem
        print('sum =', sum)
except OSError:
    print('Could not open file') 

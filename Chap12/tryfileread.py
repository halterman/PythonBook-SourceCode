#  Sum the values in a text file containing integer values
try:
    f = open('mydata.dat')
except OSError:
    print('Could not open file')
else:   # File opened properly
    sum = 0
    try:
        for line in f:
            sum += int(line)
        f.close()  # Close the file if no exception
    except Exception as er:
        print(er)  # Show the problem
        f.close()  # Close the file if exception
    print('sum =', sum)

#  Sum the values in a text file containing integers
try:
    f = open('mydata.dat')
except OSError:
    print('Could not open file') 
else:
    sum = 0
    try:
        for line in f:
            sum += int(line)
    except Exception as er:
        print(er)  # Show the problem
    finally:
        f.close()  # Close the file
    print('sum =', sum)

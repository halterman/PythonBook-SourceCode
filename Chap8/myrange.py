def myrange(arg1, arg2=None, step=1):
    if arg2 != None:   # Do we have at least two arguments?
        begin = arg1
        end = arg2
    else:      # We must have just one argument 
        begin = 0   # Begin value is zero by default
        end = arg1
    i = begin
    while i != end:
        yield i
        i += step


print('0 to 9:', end=' ')
for i in myrange(10):
    print(i, end=' ')
print()

print('1 to 10:', end=' ')
for i in myrange(1, 11):
    print(i, end=' ')
print()

print('2 to 18 by twos:', end=' ')
for i in myrange(2, 20, 2):
    print(i, end=' ')
print()

print('20 down to 2 by twos:', end=' ')
for i in myrange(20, 0, -2):
    print(i, end=' ')
print()

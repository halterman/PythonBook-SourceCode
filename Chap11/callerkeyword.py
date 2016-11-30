def f(a, b, c):
    print('a =', a, ' b =', b, ' c =', c)


f(1, 2, 3)                      # Pass three parameters
dict = {}
dict['b'] = 22
dict['a'] = 11
dict['c'] = 33
f(**dict)
f(**{'a':10, 'b':20, 'c':30})   # Pass a dictionary

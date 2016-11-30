#  Data structure size
size = 1000

#  Make a big set
S = {x**2 for x in range(size)}
#  Make a big list
L = [x**2 for x in range(size)]

#  Verify the type of S and L
print('Set:', type(S), ' List:', type(L))

from time import clock

#  Search size
search_size = 1000000

#  Time list access
start_time = clock()
for i in range(search_size):
    if i in L:
        pass
stop_time = clock()
print('List elapsed:', stop_time - start_time)

#  Time set access
start_time = clock()
for i in range(search_size):
    if i in S:
        pass
stop_time = clock()
print('Set elapsed:', stop_time - start_time)
